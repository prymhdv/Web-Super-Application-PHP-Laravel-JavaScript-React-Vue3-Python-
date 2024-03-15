@extends('layouts.master')
@section('content')
<div class="JStest">
    <div class="container">

        <h1 id="jsTitle" draggable="true">-------------------Java Script Basic
            <span id="date">2024</span>-------------------<span id="insertlocation"></span>
            <h1>
                <br />
                <script>
                    getany();
                    pageTitle = document.getElementById("jsTitle").innerHTML;
                    //document.write(pageTitle);
                    // document.getElementById("insertlocation").innerHTML=  "Hello2";
                    document.getElementById("jsTitle").style.fontWeight = "bold";
                </script>
                <br />
                <button onClick="solo('</br>its new javascript coding')">Click to see</button>
                <div style="margin:10px;">
                    <div id="TargetDiv" class="text-center" ondragover="allowDrop(event)" ondrop="drop(event)" style="margin:auto;
                width:220px;
                height:60px;
                padding:10px;
                border:1px solid #999999" ;></div>
                    <!-- <h2 id="dragItem" draggable="true" ondragstart="drag(event)"> hello </h2> -->
                    <img id="dragItem" src="img/aa.jpg" width="200" height="50" draggable="true" ondragstart="drag(event)" />
                </div>

                <div style="margin:10px;">
                    <form name="calc">
                        <input type="text" name="n1">+
                        <input type="text" name="n2">
                        <br /><br />
                        <button type="button" onclick='calculate()'>calculate</button>
                    </form>
                    <p class="text-center"> the answer is: <span id="total"></span></p>
                </div>
                <div class="ltr">
                    <h1> custom video controls</h1>
                    <video  id="video" controls width=320 height=240 poster="media/VolumeDataAlongSurfaceExample_01.png" onloadedmetadata="setDuration()" ontimeupdate="updateTime()">
                        <source src="media/video.webm" type="video/webm" />
                        <!-- <source src="media/VolumeDataAlongSurfaceExample_01.png" type="photo"/> -->
                        this text should only apper when your browser dose not support video playback.
                    </video>
                    <br />
                    <button type="button" onclick='playVideo()'>play</button>
                    <button type="button" onclick='pauseVideo()'>pause</button>
                    <button type="button" onclick='stopVideo()'>stop</button>
                    <button type="button" onclick='fwdVideo()'>forward</button>
                    <button type="button" onclick='revVideo()'>reverse</button>
                    <br>
                    <p class=text-center> total duration: <span id="totalTime"> x </span> Secounds</p>
                    <p class=text-center> current time: <span id="timeText"> 0 </span> Secounds</p>

                </div>
                <div>
                    <h1 class="text-center"> custom Audio controls</h1>
                    <audio controls id="audio" onloadedmetadata="getAudioVolume()">
                        <source src="media/RockDrums-44p1-stereo-11secs.mp3" type="audio/mpeg" />
                        Your browser dose not support the audio element.
                    </audio>
                    <br>
                    <p class="text-center"> current volume: <span id="volume">xx</span></p>
                    <button type="button" onclick='volumeDown()'>volumeDown</button>
                    <button type="button" onclick='volumeUp()'>volumeUp</button>
                    <br>
                    <img id="button" src="media/drawable-xhdpi/ic_menu_play_clip.png" onClick="PlayPause()" />
                </div>
                <h1 id="jsTitle" draggable="true">-------------------Java Script Basic-------------------<h1>
    </div>
    <div class="content text-center">
        <h1 id="jsTitle" draggable="true">-------------------CSS Basic-------------------<h1>
                <div class="content">
                    <div class="top-Squre">
                    </div>
                    <div class="bottom-Squre">
                    </div>
                </div>

                <img class="imgescss" src="media/drawable-xhdpi/ic_menu_play_clip.png" />
                <h1 class=" someH1 test-center"> SOME TEST</h1>


                <div class="contetn2 text-center">
                    <p>
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hellohello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hellohello hello hello hello hello hello
                        hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello
                    </p>


                </div>



                <h1 id="jsTitle" draggable="true">-------------------CSS Basic end -------------------<h1>

                        <h1 id="jsTitle" draggable="true">-------------------Canvas Basic start -------------------<h1>
                                <canvas id="testCanvas" width="300px" height="300px">your browser cannot support canvas graphics </canvas>

                                <h1 id="jsTitle" draggable="true">-------------------Canvas Basic 2-------------------<h1>

                                        <canvas id="test2Canvas" width="300px" height="300px">your browser cannot support canvas graphics.</canvas>


                                        <canvas id="test3Canvas" width="300px" height="300px">your browser cannot support canvas graphics.</canvas>


                                        <canvas id="test4Canvas" width="500px" height="300px">your browser cannot support canvas graphics.</canvas>

                                        <h1 id="jsTitle" draggable="true">-------------------Canvas Basic 3-------------------<h1>
                                                <canvas id="test5Canvas" width="300px" height="300px">your browser cannot support canvas graphics.</canvas>

                                                <h1 id="jsTitle" draggable="true">-------------------Canvas Basic 3 Pattern-------------------<h1>
                                                        <img id="pattern" src="media/star.png" width="51" height="50" style="display:none" />
                                                        <canvas id="test6Canvas" width="300px" height="300px">your browser cannot support canvas graphics.</canvas>

                                                        <h1 id="jsTitle" draggable="true">-------------------Canvas Basic 4 Pattern-------------------<h1>
                                                                <a href="{{  route('main.index2') }}">
                                                                    <canvas id="test7Canvas" width="300px" height="300px">your browser cannot support canvas graphics.</canvas>
                                                                </a>
                                                                <canvas id="test8Canvas" width="300px" height="300px" style="border: 1px solid black">your browser cannot support canvas graphics.</canvas>

                                                                <script>
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftestCanvas() {
                                                                        var canvas = document.getElementById("testCanvas");
                                                                        var context = canvas.getContext("2d");

                                                                        context.beginPath();
                                                                        context.rect(10, 10, 250, 150);


                                                                        context.fillStyle = "green";
                                                                        context.fill();
                                                                        context.strokeStyle = "blue";
                                                                        context.lineWidth = 8;
                                                                        context.lineCap = "round"
                                                                        context.stroke();

                                                                        context.beginPath();
                                                                        context.moveTo(50, 50);
                                                                        context.lineTo(50, 250);
                                                                        context.lineTo(250, 150);
                                                                        context.closePath();

                                                                        context.fillStyle = "red";
                                                                        context.fill();
                                                                        context.lineWidth = 18;
                                                                        context.lineJoin = "round";
                                                                        context.strokeStyle = "black";
                                                                        context.stroke();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest2Canvas() {
                                                                        var canvas = document.getElementById("test2Canvas");
                                                                        var context = canvas.getContext("2d");

                                                                        context.beginPath();
                                                                        context.moveTo(50, 50);
                                                                        context.lineTo(50, 200);
                                                                        context.arcTo(50, 250, 100, 250, 50);
                                                                        context.lineTo(250, 250);
                                                                        context.closePath();

                                                                        context.stroke();
                                                                        context.fill();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest3Canvas() {
                                                                        var canvas = document.getElementById("test3Canvas");
                                                                        var context = canvas.getContext("2d");

                                                                        var startAng = 280 * Math.PI / 180;
                                                                        var endAng = 360 * Math.PI / 180;

                                                                        context.beginPath();
                                                                        context.arc(150, 150, 100, startAng, endAng, true);

                                                                        context.stroke();
                                                                        context.fillStyle = "green";
                                                                        context.fill();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest4Canvas() {
                                                                        var canvas = document.getElementById("test4Canvas");
                                                                        var context = canvas.getContext("2d");


                                                                        context.beginPath();
                                                                        context.moveTo(50, 150);
                                                                        //context.quadraticCurveTo(10,300,250,150);
                                                                        // context.bezierCurveTo(100,300,250,300,250,150);
                                                                        // context.bezierCurveTo(250,0,400,0,450,150);

                                                                        context.bezierCurveTo(100, 300, 250, 300, 250, 150);
                                                                        context.bezierCurveTo(250, 0, 400, 0, 450, 150);
                                                                        context.lineWidth = 8;
                                                                        context.strokeStyle = "blue";
                                                                        context.stroke();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest5Canvas() {
                                                                        var canvas = document.getElementById("test5Canvas");
                                                                        var context = canvas.getContext("2d");


                                                                        context.beginPath();
                                                                        context.rect(10, 10, 280, 130);

                                                                        var grad = context.createLinearGradient(50, 0, 250, 0);
                                                                        grad.addColorStop(0, "red");
                                                                        grad.addColorStop(.3, "yellow");
                                                                        grad.addColorStop(1, "blue");
                                                                        context.fillStyle = grad;
                                                                        context.fill();

                                                                        context.beginPath();
                                                                        context.rect(10, 160, 280, 130);

                                                                        var grad2 = context.createRadialGradient(150, 250, 5, 150, 250, 150);
                                                                        grad2.addColorStop(0, "red");
                                                                        grad2.addColorStop(.3, "yellow");
                                                                        grad2.addColorStop(1, "blue");
                                                                        context.fillStyle = grad2;
                                                                        context.fill();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest6Canvas() {
                                                                        var canvas = document.getElementById("test6Canvas");
                                                                        var context = canvas.getContext("2d");

                                                                        var img = document.getElementById("pattern");
                                                                        var patt = context.createPattern(img, "repeat");

                                                                        var startAnd = 0 * Math.PI / 180;
                                                                        var endAng = 360 * Math.PI / 180;

                                                                        context.beginPath();
                                                                        context.arc(150, 150, 100, startAnd, endAng, false);

                                                                        context.shadowOffsetX = 20;
                                                                        context.shadowOffsetY = 20;
                                                                        context.shadowBlur = 20;
                                                                        context.shadowColor = "gray";



                                                                        context.fillStyle = patt;
                                                                        context.fill();
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest7Canvas() {
                                                                        var canvas = document.getElementById("test7Canvas");
                                                                        var context = canvas.getContext("2d");
                                                                        context.translate(15, 4);
                                                                        context.rotate(6 * Math.PI / 180);
                                                                        context.scale(1.2, 1.2);

                                                                        var x = canvas.width / 2;
                                                                        var y = canvas.height / 2;
                                                                        context.font = "bold 30pt Arial";
                                                                        context.textAlign = "center";
                                                                        context.textBaseline = "middle"
                                                                        context.fillStyle = "red";
                                                                        context.fillText("Go Home", x, y);

                                                                        context.strokeStyle = "black";
                                                                        context.lineWidth = 3;
                                                                        context.strokeText("Go Home", x, y);
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    function ftest8Canvas() {
                                                                        var canvas = document.getElementById("test80Canvas");
                                                                        var context = canvas.getContext("2d");
                                                                        context.translate(15, 4);
                                                                        context.rotate(6 * Math.PI / 180);
                                                                        context.scale(1.2, 1.2);

                                                                        var x = canvas.width / 2;
                                                                        var y = canvas.height / 2;
                                                                        context.font = "bold 30pt Arial";
                                                                        context.textAlign = "center";
                                                                        context.textBaseline = "middle"
                                                                        context.fillStyle = "red";
                                                                        context.fillText("Go Home", x, y);

                                                                        context.strokeStyle = "black";
                                                                        context.lineWidth = 3;
                                                                        context.strokeText("Go Home", x, y);
                                                                    }
                                                                    // ------------------------------------------------------------------------------------------
                                                                    var xLoc = 20;
                                                                    var yLoc = 20;
                                                                    window.requestAnimFrame = (function(callback) {
                                                                        return window.requestAnimationFrame ||
                                                                            window.webkitRequestAnimationFrame ||
                                                                            window.mozRequestAnimationFrame ||
                                                                            window.oRequestAnimationFrame ||
                                                                            window.msRequestAnimationFrame ||
                                                                            function(callback) {
                                                                                window.setTimeout(callback, 1000 / 60);
                                                                            };
                                                                    })();

                                                                    function animate() {
                                                                        var canvas = document.getElementById("test8Canvas");
                                                                        var context = canvas.getContext("2d");

                                                                        // clear the canvas
                                                                        context.clearRect(0, 0, canvas.width, canvas.height);
                                                                        if (xLoc < 400) {
                                                                            xLoc++;
                                                                            yLoc++;
                                                                        }

                                                                        // draw the next frame
                                                                        context.beginPath();
                                                                        context.rect(xLoc, yLoc, 100, 100);
                                                                        context.fillStyle = "blue";
                                                                        context.fill();
                                                                        // request a new frame
                                                                        requestAnimFrame(function() {
                                                                            animate();
                                                                        });
                                                                    }

                                                                    function canvaser() {


                                                                        ftestCanvas();
                                                                        ftest2Canvas();
                                                                        ftest3Canvas();
                                                                        ftest4Canvas();
                                                                        ftest5Canvas();
                                                                        ftest6Canvas();
                                                                        ftest7Canvas();
                                                                        ftest8Canvas();
                                                                        animate();

                                                                    };
                                                                </script>

                                                                <h1 id="jsTitle" draggable="true">-------------------Canvas Basic end-------------------<h1>

                                                                        <h1 id="jsTitle" draggable="true">-------------------Transform Basic-------------------<h1>

                                                                                <img class="rotated" src="media/sample.jpg" width="151" height="150" />


                                                                                <h1 id="jsTitle" draggable="true">-------------------Transform Basic end-------------------<h1>
                                                                                        <h1 id="jsTitle" draggable="true">-------------------geolocation Basic -------------------<h1>
                                                                                                <div class="text-center">
                                                                                                    <p class="text-center"><strong>your latitude: </strong><span id="latitude"> 000</span></p>

                                                                                                    <p class="text-center"><strong>your longitude: </strong><span id="longitude"> 000</span></p>

                                                                                                    <p class="text-center"><button onClick="getPosition()">click for your location</button></p>

                                                                                                    <div id="map"></div>

                                                                                                    <script>
                                                                                                        function getPosition() {
                                                                                                            if (navigator.geolocation) {


                                                                                                                navigator.geolocation.getCurrentPosition(fshowPosition, fpossitionError);

                                                                                                                // navigator.geolocation.getCurrentPosition(successCallback, errorCallback, {
                                                                                                                //     timeout: 1000
                                                                                                                // });
                                                                                                                //
                                                                                                                //button.addEventListener("click", () => {
                                                                                                                navigator.geolocation.getCurrentPosition((position) => {
                                                                                                                    let lat = position.coords.latitude;
                                                                                                                    let long = position.coords.longitude;

                                                                                                                    // latText.innerText = lat.toFixed(2);
                                                                                                                    // longText.innerText = long.toFixed(2);

                                                                                                                    document.getElementById("latitude").innerHTML = lat.toFixed(2);;
                                                                                                                    document.getElementById("longitude").innerHTML = long.toFixed(2);

                                                                                                                    var latlong = position.coords.latitude + "," + position.coords.longitude;
                                                                                                                    var mapURL = "http://maps.googleapis.com/maps/api/staticmap?center=" + latlong +
                                                                                                                        "&markers=color:blue%7Clabel:1%7C" + latlong +
                                                                                                                        "&zoom=14&size=400*300&sensor=false";
                                                                                                                    document.getElementById("map").innerHTML = "<img src='" + mapURL + "'/>";

                                                                                                                });
                                                                                                                //});
                                                                                                                //----------------------

                                                                                                                //-----------------------------------------------
                                                                                                                fshowPosition(position);
                                                                                                                fpossitionError(fpossitionError);
                                                                                                                alert(" getPosition :: the browser suppoert geolocation.");

                                                                                                            } else {
                                                                                                                alert("the browser dose not suppoert geolocation.");
                                                                                                            }
                                                                                                        }

                                                                                                        function fshowPosition(position) {
                                                                                                            alert("showPosition :: the browser  suppoert geolocation. ");
                                                                                                            document.getElementById("latitude").innerHTML = position.coords.latitude;
                                                                                                            document.getElementById("longitude").innerHTML = position.coords.longitude;

                                                                                                            var latlong = position.coords.latitude + "," + position.coords.longitude;
                                                                                                            var mapURL = "http://maps.googleapis.com/maps/api/staticmap?center=" + latlong +
                                                                                                                "&markers=color:blue%7Clabel:1%7C" + latlong +
                                                                                                                "&zoom=14&size=400*300&sensor=false";
                                                                                                            document.getElementById("map").innerHTML = "<img src='" + mapURL + "'/>";
                                                                                                        }

                                                                                                        function fpossitionError(erorr) {
                                                                                                            if (erorr.code == error.TIMEOUT) {
                                                                                                                alert("sorry can shown TIMEOUT");
                                                                                                            }
                                                                                                            if (erorr.code == error.POSITION_UNAVAILBLE) {
                                                                                                                alert("sorry can shown GPS");
                                                                                                            }
                                                                                                            if (erorr.code == error.PERMISSION_DENIED) {
                                                                                                                alert("sorry can shown NOT ALLOW");
                                                                                                            }
                                                                                                            if (erorr.code == error.UKNOWN_ERROR) {
                                                                                                                alert("sorry can shown UNknown");
                                                                                                            }

                                                                                                        }
                                                                                                    </script>
                                                                                                </div>

                                                                                                <h1 id="jsTitle" draggable="true">-------------------geolocation Basic 2-------------------<h1>
                                                                                                        <div class="distance">
                                                                                                            <button onClick="getDistance()">the distance: <span id="distancer">xx</span></button>
                                                                                                            <script>
                                                                                                                function getDistance() {
                                                                                                                    var pos;
                                                                                                                    navigator.geolocation.getCurrentPosition(pos);
                                                                                                                    var lat = pos.coords.latitude;
                                                                                                                    var long = pos.coords.longitude;

                                                                                                                    var lat2 = -37.789456 * Math.PI / 180;
                                                                                                                    var long2 = -122.789456 * Math.PI / 180;

                                                                                                                    var a = (long2 - long) * Math.cos((lat + lat2) / 2);
                                                                                                                    var b = (lat2 - lat);

                                                                                                                    var distance = Math.round(Math.sqrt(a * a + b * b) * 6375);
                                                                                                                    document.getElementById("distancer").innerHTML = distance;


                                                                                                                }
                                                                                                            </script>
                                                                                                        </div>
                                                                                                        <h1 id="jsTitle" draggable="true">-------------------geolocation Basic end-------------------<h1>

                                                                                                                <h1 id="jsTitle" draggable="true">-------------------mobile app Basic-------------------<h1>
                                                                                                                        <div class="row text-cnter">

                                                                                                                            <p id="greeting">greeting</p>

                                                                                                                            firstname: <br /><input type="text" id="firstname" /><br />
                                                                                                                            <button onClick="enterName()">enter name</button>
                                                                                                                            <br /><br />

                                                                                                                            number:<br /><input type="number" id="number" /><br />
                                                                                                                            <button onClick="addToTotal()">add number to total</button>
                                                                                                                            <br />

                                                                                                                            <p> total = <span id="total">0</span></p>

                                                                                                                            <button onClick="clearTotal()">clear total</button>

                                                                                                                            <script>
                                                                                                                                function onloader_forms() {
                                                                                                                                    //localStorage.firstName = "bob";

                                                                                                                                    // document.getElementById("greeting").innerHTML = "Hi " + localStorage.firstName;
                                                                                                                                    // document.getElementById("total").innerHTML = localStorage.total;

                                                                                                                                    document.getElementById("greeting").innerHTML = "Hi " + sessionStorage.firstName;
                                                                                                                                    document.getElementById("total").innerHTML = sessionStorage.total;
                                                                                                                                }

                                                                                                                                function enterName() {
                                                                                                                                    sessionStorage.firstName = document.getElementById("firstname").value;
                                                                                                                                }

                                                                                                                                function addToTotal() {
                                                                                                                                    var total = 0;
                                                                                                                                    var oldtotal = Number(sessionStorage.total);
                                                                                                                                    if (oldtotal > 0) {
                                                                                                                                        total = oldtotal + Number(document.getElementById("number").value);
                                                                                                                                    } else {
                                                                                                                                        total = Number(document.getElementById("number").value);
                                                                                                                                    }
                                                                                                                                    document.getElementById("total").innerHTML = total;
                                                                                                                                    sessionStorage.total = total;
                                                                                                                                }

                                                                                                                                function clearTotal() {
                                                                                                                                    sessionStorage.clear();
                                                                                                                                }
                                                                                                                            </script>
                                                                                                                        </div>


                                                                                                                        <h1 id="jsTitle" draggable="true">-------------------mobile app Basic end-------------------<h1>
                                                                                                                                <div class="media">
                                                                                                                                    <span id="names">pp</span>
                                                                                                                                    <button id="press" onclick="listNames()">press</button>
                                                                                                                                    <div id="listofnames"></div>
                                                                                                                                </div>
                                                                                                                                <h1 id="jsTitle" draggable="true">-------------------mobile app Basic end-------------------<h1>
                                                                                                                                        <script>
                                                                                                                                            var names = ["sam", "pry", "bob"];
                                                                                                                                            names.push("jack");
                                                                                                                                            window.onload = function() {
                                                                                                                                                document.getElementById("names").innerHTML = names[3];
                                                                                                                                                canvaser();
                                                                                                                                                onloader_forms();
                                                                                                                                                listNames();
                                                                                                                                            }

                                                                                                                                            function listNames() {
                                                                                                                                                var output = "the name are: <br/>";
                                                                                                                                                for (var i = 0; i < names.length; i++) {
                                                                                                                                                    output += names[i] + "<br/>";
                                                                                                                                                }
                                                                                                                                                document.getElementById("listofnames").innerHTML = output;

                                                                                                                                            }
                                                                                                                                        </script>


    </div>
</div>
<hr>
<hr>
@endsection