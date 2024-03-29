<<<<<<< HEAD
PyImageStream - Python WebSocket Image Stream
=============================================

Server which streams images (JPEG) from a WebCam (USB camera or Raspberry Pi Camera Module) via a WebSocket. Also
includes a simple JavaScript client to show the video in a Web Browser.

I've implemented this for streaming live images of my Aquarium from a Raspberry Pi 3 to my smartphone (or tablet or PC)
when I'm on vacation to check on my fish :tropical_fish:. For this I want to see high resolution images (e.g. the full
1920x1080 pixels the Raspberry Pi Camera can provide), even if the connection speed is slow. It is fine to see only a
few images per second, if I'm on a slow network, but if it is fast I want to see a more smooth video.

For my use case this implementation has several advantages over other existing Web video streaming solutions:
* Supports high resolution images (video) even if the connection speed is slow by automatically adapting the framerate.
* A simple pull approach ensures this adaptive framerate: The client will ask the server only for a new image once it
  has fully loaded the previous one. That way the images will never lag behind for a longer time or appear corrupted.
  (In comparison to fixed framerate/bandwith Motion JPEG (MJPEG) solutions like
  [motion](https://motion-project.github.io/) / [motioneye](https://github.com/ccrisan/motioneye/wiki),
  [MJPEG-streamer](https://sourceforge.net/projects/mjpg-streamer/) and also MPEG1 solutions like
  [JSMPEG](https://github.com/phoboslab/jsmpeg) / [pistreaming](https://github.com/waveform80/pistreaming).)
* Works on all modern Browsers (including Mobile) that support WebSockets.
* Easier to set up and configure and better supported by Web browsers (at the time of this writing) than more advanced
  adaptive video streaming methods like HLS, MPEG-DASH, WebRTC.
* Works with the Raspberry Pi Camera Module and with almost any USB camera (supported by Linux / pygame). (In comparison
  to the otherwise very nice [RPi-Cam-Web-Interface](http://elinux.org/RPi-Cam-Web-Interface), which unfortunately only
  works with the Raspberry Pi Camera.)
* Automatically turns off the camera if no client is connected. (To safe energy, camera lifetime and CPU usage. And then
  you also know that someone watches if you are at home and the camera LED suddenly turns on. :wink:)
* Doesn't write images / video to disk (to not shorten the lifetime of the SD card) but encodes and sends them in
  memory.
* Sends the data efficiently in binary format and not Base64 encoded (in comparison to the otherwise very similar
  [hello-websocket](https://github.com/vmlaker/hello-websocket)).
* Fully open source. (In comparison to [UV4L](https://www.linux-projects.org/uv4l/), which seems to be
  closed-source. :scream:)

Disadvantages:

* For higher resolutions it will never achieve a high framerate, because it's not using an efficient
  Video codec (like H.264).
* Doesn't work well with many clients connecting simultanously, because it will capture new images and send them to
  each client separately (i.e. the framerate will become slower). This isn't a problem for my use case as I and my
  girlfriend will be the only ones connecting to our aquarium video.

Prerequisites
-------------

### Install dependencies

The commands below assume you are using Rasbian Jessie on a Raspberry Pi. Installation of dependencies might be
slightly different on other Linux distributions. For that please refer to the installation instructions of each of
these packages. This project has not yet been tested on other operating system, like Windows, but should probably work
there too.

[Python 3](https://www.python.org/)

    sudo apt install python3
    
PIP for installing Python packages:

    sudo apt-get install python3-pip

[Tornado Web server](http://www.tornadoweb.org/)

    sudo pip3 install tornado

[Python Imaging Library](https://pypi.python.org/pypi/PIL) (or the [Pillow](https://python-pillow.org/) fork)

    sudo apt install python3-pil

[Pygame](https://www.pygame.org/) (used for capturing images from a Webcam)

    sudo apt install python3-pygame
    
[git](https://git-scm.com/) (to clone this repository)

    sudo apt install git

### Connect your Webcam

The Webcam has to be compatible with Video4Linux2 and should appear as /dev/video0 in the filesystem.
Most USB Webcams support the UVC standard and should work just fine.
The [Raspberry Pi Camera Module](https://www.raspberrypi.org/documentation/usage/camera/) can be made available as a
V4L2 device by loading a kernel module:

    sudo modprobe bcm2835-v4l2
    
To permanently load this module (so that it also works after a reboot) add the line `bcm2835-v4l2` to `/etc/modules`.

Installation
------------

Clone the repository to some directory and change to that directory:

    git clone https://github.com/Bronkoknorb/PyImageStream.git
    cd PyImageStream

Start with

    python3 main.py

The stream can then be watched on: http://YOUR_HOST:8888/ (where YOUR_HOST is your host name or IP address or localhost
on the same machine).

Configuration
-------------

`main.py` can be started with a number of optional arguments:
```
usage: main.py [-h] [--port PORT] [--camera CAMERA] [--width WIDTH]
               [--height HEIGHT] [--quality QUALITY] [--stopdelay STOPDELAY]

Start the PyImageStream server.

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           Web server port (default: 8888)
  --camera CAMERA       Camera index, first camera is 0 (default: 0)
  --width WIDTH         Width (default: 640)
  --height HEIGHT       Height (default: 480)
  --quality QUALITY     JPEG Quality 1 (worst) to 100 (best) (default: 70)
  --stopdelay STOPDELAY
                        Delay in seconds before the camera will be stopped
                        after all clients have disconnected (default: 7)
```

If you have multiple cameras connected, then simply start multiple instances of this server on different ports.

In the file `static/client.js` you can configure the maximum framerate that the client will try to load
and display (default: 24 frames per second).

Autostart
---------

To automatically start the server when your machine is rebooted, execute:

    crontab -e

... and then add the following line to the crontab:

    @reboot sleep 5 && /home/pi/software/PyImageStream/start.sh

Replace the path of the script with the location where you installed it. You can also add any of the optional arguments to the line.

Logrotate
---------

When starting the server using the `start.sh` command it will write to a `server.log` file. To avoid that this log file grows infinite create the following logrotate rule as `/etc/logrotate.d/PyImageStream`:

```
/home/pi/software/PyImageStream/server.log {
   weekly
   rotate 4
   compress
   missingok
   copytruncate
}
```
Replace the path of the logfile with the location where you installed it.

Security
--------

To enable encryption (HTTPS) and password authentication you can setup another Web server
(like [nginx](https://nginx.org/)) as a reverse proxy before this server.

This is the relevant part from a nginx configuration file that I use to proxy my PyImageStream:

    location ^~ /cam1/websocket {
        proxy_pass http://10.0.0.16:8888/websocket;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location ~ ^/cam1/(.*)$ {
        proxy_pass http://10.0.0.16:8888/$1;
        include /etc/nginx/proxy_params;
    }

It will make the camera available under http://YOUR_HOST/cam1/

To setup authentication and HTTPS please refer to the nginx documentation. If you have a domain name or are using a
Dynamic DNS service, then you can get free HTTPS certificates from [letsencrypt](https://letsencrypt.org/).

Alternatively you could also configure authentication and HTTPS for the internally used Python Tornado Web server.
I haven't tried that yet, but the Tornado Web server documentation should help with that.

Happy?
------

If you are using this project, I'd be happy to hear! Please Star the repository (button in the top right) or drop me a
mail (dev@hermann.czedik.net)!

If you have problems or questions then please open an
[Issue on github](https://github.com/Bronkoknorb/PyImageStream/issues).

Feel free to fork the repository and create pull requests for improvements and new features.

License
-------

See [LICENSE](LICENSE).

Author
------

Hermann Czedik-Eysenberg  
dev@hermann.czedik.net
=======
# PyControl
>>>>>>> 2d51776c89ad9a50f5f8b457e97e2755f24491cf
