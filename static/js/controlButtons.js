
var testText=document.getElementById("test1");


document.getElementById("forwardButton").addEventListener("mousedown", forwardButtonClicked);
document.getElementById("backwardButton").addEventListener("mousedown", backwardButtonClicked);
document.getElementById("rightButton").addEventListener("mousedown", rightButtonClicked);
document.getElementById("leftButton").addEventListener("mousedown", leftButtonClicked);

document.getElementById("forwardButton").addEventListener("mouseup", forwardButtonReleased);
document.getElementById("backwardButton").addEventListener("mouseup", backwardButtonReleased);
document.getElementById("rightButton").addEventListener("mouseup", rightButtonReleased);
document.getElementById("leftButton").addEventListener("mouseup", leftButtonReleased);

if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) )
{
	testText.textContent=navigator.userAgent;
}
else
{
	
	
	console.log(navigator.platform);
	testText.textContent="inny";
}



function forwardButtonClicked()
{
	test1.textContent="forward";
        console.log("onclcicked");
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
	test1.textContent="forrel";
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



