{/* <script> */ }
/* in side script tag */
// alert("Jave scripot created this massage");
// Writing into an HTML element, using innerHTML.
// Writing into the HTML output using document.write().
// Writing into an alert box, using window.alert().
// Writing into the browser console, using console.log().
//---------------------------------------------------

function solo(massage) {
    document.writeln(" the document <strong>write</strong> is test inf");
    varA = "Hello ";
    document.writeln("</br>" + varA + " Pourya: " + "<strong>" + massage + "</strong>");
    document.writeln("</br>", 5 + "8", "</br>");

}
//---------------------------------------------------
function showDate() { }

//---------------------------------------------------
function getany() {
    date = document.getElementById("date").innerHTML;
    if (date > 2023) {
        document.write("</br>", "<strong>", date, "</strong>", "<strong>is grater than 2023 </strong>", "</br>");
    } else {

        document.write("<br/>", "<strong>", date, "</strong>", "<strong>isnt grater than 2023 </strong>", "</br>");
    }
    //---------------------------------------------------
    for (i = 0; i < 3; i++) {
        document.write("<br/>", "<strong>", date++, "</strong>");
    }
}
//---------------------------------------------------
function drag(e) {
    e.dataTransafer.setData("Text", e.target.id);
}

function allowDrop(e) {
    e.preventDefault();
}

function drop(e) {
    e.preventDefault();
    dragItem = e.dataTransafer.getData("Text");
    e.target.appendChild(document.getElementById(dragItem));
}
//---------------------------------------------------
function calculate() {
    FormData = document.forms['calc'];
    var n1 = FormData.elements['n1'].value;
    var n1 = Number(n1);
    var n2 = FormData.elements['n2'].value;
    var n2 = Number(n2);
    var total = n1 + n2;
    document.getElementById('total').innerHTML = total;
}
//---------------------------------------------------

// vid = document.getElementById("video"); global not worked
function playVideo() {
    var vid = document.getElementById("video");
    vid.play();
}
function pauseVideo() {
    var vid = document.getElementById("video");
    vid.pause();
}
function setDuration() {
    var vid = document.getElementById("video");
    document.getElementById("totalTime").innerHTML = Math.round(vid.duration);
}

function updateTime() {
    var vid = document.getElementById("video");
    document.getElementById("timeText").innerHTML = Math.round(vid.currentTime);
}
function stopVideo() {
    var vid = document.getElementById("video");
    vid.pause();
    vid.currentTime = 0;
}
function fwdVideo() {
    var vid = document.getElementById("video");
    vid.currentTime++;
}
function revVideo() {
    var vid = document.getElementById("video");
    vid.currentTime--;

    // // vid.set("Accept-Ranges", "bytes");
    // if (vid.seekable.length > 0) {
    //     //vid.currentTime--;
    //     vid.setDuration(5);
    //   }


}
//---------------------------------------------------
function getAudioVolume() {
    var Aud = document.getElementById("audio");
    document.getElementById("volume").innerHTML = Aud.volume * 100;
}
function volumeDown() {
    var Aud = document.getElementById("audio");
    Aud.volume -= .1;
    document.getElementById("volume").innerHTML = Math.round(Aud.volume * 100, 2);

}
function volumeUp() {
    var Aud = document.getElementById("audio");
    Aud.volume += .1;
    document.getElementById("volume").innerHTML = Math.round(Aud.volume * 100, 2);

}
//---------------------------------------------------
function PlayPause() {

    var Aud = document.getElementById("audio");
    var vid = document.getElementById("video");
    if (Aud.paused) {
        Aud.play();
        vid.play();
        document.getElementById("button").src = "media/drawable-xhdpi/ic_media_pause.png";
    }
    else {
        Aud.pause();
        vid.pause();
        document.getElementById("button").src = "media/drawable-xhdpi/ic_menu_play_clip.png";
    }
}

//---------------------------------------------------
{/* </script> */ }

{/* <script data-cfasync="false" type="text/javascript" src="https://code.jquery.com/jquery.min.js"></script> */ }
{/* <script> */ }
// var $a = $.noConflict(true);
// $a(window).scroll(function () {
//     if ($a(window).scrollTop() >= 300) {
//         $a('.cg-menu-below').addClass('fixed-header');
//     } else {
//         $a('.cg-menu-below').removeClass('fixed-header');
//     }
// });
{/* </script> */ }
//---------------------------------------------------
//---------------------------------------------------
//---------------------------------------------------
//---------------------------------------------------
//---------------------------------------------------