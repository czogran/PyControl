
var testText=document.getElementById("test1");

document.getElementById("forwardButton").addEventListener("click", forwardButtonClicked);

function forwardButtonClicked()
{
		test1.textContent="forward";
        console.log("onclcicked");
        ws.send("forward");
}

document.getElementById("backwardButton").addEventListener("click", backwardButtonClicked);

function backwardButtonClicked()
{
	test1.textContent="backward";
        console.log("clicked");
        ws.send("forward");
}
document.getElementById("rightButton").addEventListener("mousedown", rightButtonClicked);

function rightButtonClicked()
{
	test1.textContent="right";
        console.log("mousedown");
        ws.send("forward");
}
