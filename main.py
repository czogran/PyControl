#!/usr/bin/env python3

import argparse
import os
import io

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect

from PIL import Image

from engine import engines_chassis
from camera import camera

import logging
import json

parser = argparse.ArgumentParser(description='Start the PyImageStream server.')

parser.add_argument('--port', default=8888, type=int, help='Web server port (default: 8888)')
parser.add_argument('--camera', default=0, type=int, help='Camera index, first camera is 0 (default: 0)')
parser.add_argument('--width', default=640, type=int, help='Width (default: 640)')
parser.add_argument('--height', default=480, type=int, help='Height (default: 480)')
parser.add_argument('--quality', default=70, type=int, help='JPEG Quality 1 (worst) to 100 (best) (default: 70)')
parser.add_argument('--stopdelay', default=7, type=int, help='Delay in seconds before the camera will be stopped after '
                                                             'all clients have disconnected (default: 7)')
args = parser.parse_args()




camera = camera.Camera(args.camera, args.width, args.height, args.quality, args.stopdelay)
engines = engines_chassis.EnginesChassis()


class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
		#PeriodicCallback(self.keep_alive, 20000).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print ('trying to connect')
       
        self.ws = yield websocket_connect(self.url)
        self.ws.write_message('{"author":"rpi","rest":"post","type":"logging","value":"rpi"}')
        
        print ("connected")
        camera.request_start()
        self.run()
        
    @gen.coroutine
    def run(self):
        while True:
            message =  yield self.ws.read_message()
            logging.info("msg: {}".format(message))
           
            try:
                content= json.loads(message)
               
                if(content["rest"]=="get"):
                    if(content["type"]=="picture"):
                        
                        jpeg_bytes = camera.get_jpeg_image_bytes()
                        self.send(jpeg_bytes)
                        logging.info("picture sended")
                elif(content["rest"]=="put"):
                    print("gere wer are")
                    try:
                        engines.move(content["value"])
                    except  Exception as e:
                        print("engines error {}".format(e))
                        logging.error("We have mistake")
            except :
                print("server disconected {}".format(message))
                engines.move("p")
                
	
    def send(self,message):
	     self.ws.write_message(message, binary="True")
		
    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")

if __name__ == "__main__":
    #client = Client("ws://192.168.1.15:8080/websocket", 5)
    client = Client("ws://79.191.233.228:80/websocket", 5)
    print("end")
