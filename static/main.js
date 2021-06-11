var alive_second = 0;
var hearbeat_rate = 1000;

function keep_alive() {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    // console.log(this);
    // console.log(this.responseText);
    if (this.readyState === 4) {
      if (this.status === 200) {
        if (this.responseText !== null) {
          var date = new Date();
          alive_second = date.getTime();
          var keep_alive_data = this.responseText;
        }
      }
    }
  };
  request.open("GET", "keep_alive", true);
  request.send();
  setTimeout('keep_alive()', hearbeat_rate);
}

function time() {
  var d = new Date();
  var current_sec = d.getTime();
  if (current_sec - alive_second > hearbeat_rate + 100) {
    document.getElementById('connection').innerHTML = "<p>Dead</p>";
  } else {
    document.getElementById('connection').innerHTML = "<p>Alive</p>"
  }

  setTimeout('time()',100);
}
