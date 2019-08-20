
var testText=document.getElementById("test1");



if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) )
{
	
	window.oncontextmenu = function(event) 
	{
		event.preventDefault();
		event.stopPropagation();
		return false;
	};
	
	document.getElementById("forwardButton").addEventListener("touchstart", forwardButtonClicked);
	document.getElementById("backwardButton").addEventListener("touchstart", backwardButtonClicked);
	document.getElementById("rightButton").addEventListener("touchstart", rightButtonClicked);
	document.getElementById("leftButton").addEventListener("touchstart", leftButtonClicked);
	
	
	
	document.getElementById("forwardButton").addEventListener("touchend", forwardButtonReleased);
	document.getElementById("backwardButton").addEventListener("touchend", backwardButtonReleased);
	document.getElementById("rightButton").addEventListener("touchend", rightButtonReleased);
	document.getElementById("leftButton").addEventListener("touchend", leftButtonReleased);
	testText.textContent=navigator.userAgent+"    test3";
}
else
{
	
	
	document.getElementById("forwardButton").addEventListener("mousedown", forwardButtonClicked);
	document.getElementById("backwardButton").addEventListener("mousedown", backwardButtonClicked);
	document.getElementById("rightButton").addEventListener("mousedown", rightButtonClicked);
	document.getElementById("leftButton").addEventListener("mousedown", leftButtonClicked);
	
	document.getElementById("forwardButton").addEventListener("mouseup", forwardButtonReleased);
	document.getElementById("backwardButton").addEventListener("mouseup", backwardButtonReleased);
	document.getElementById("rightButton").addEventListener("mouseup", rightButtonReleased);
	document.getElementById("leftButton").addEventListener("mouseup", leftButtonReleased);

	console.log(navigator.platform);
	testText.textContent="inny";
}



function forwardButtonClicked()
{
	test1.textContent="Forward";
        console.log("Onclcicked");
        ws.send("w");
}

function backwardButtonClicked()
{
	test1.textContent="backward";
        console.log("clicked");
        ws.send("s");
}

function rightButtonClicked()
{
	test1.textContent="right";
        console.log("mousedown");
        ws.send("d");
}


function leftButtonClicked()
{
	test1.textContent="left";
        console.log("mousedown");
        ws.send("a");
}


function forwardButtonReleased()
{
	test1.textContent="Forrel";
        console.log("mouseup");
        ws.send("p");
}

function backwardButtonReleased()
{
	test1.textContent="backrel";
        console.log("mouseup");
        ws.send("p");
}
function rightButtonReleased()
{
	test1.textContent="rightreleased";
        console.log("mouseup");
        ws.send("p");
}
function leftButtonReleased()
{
	test1.textContent="leftrel";
        console.log("mouseup");
        ws.send("p");
}



