var data;
function sendCommand() {
  const sendPost = async () => {
    const url = '/distance'; // the URL to send the HTTP request to
    const method = 'POST';
    const response = await fetch(url, { method });
    console.log(response);
    data = await response.text(); // or response.json() if your server returns JSON
    console.log(data);

  }

  sendPost();
  document.getElementById('distance').innerHTML = `<p> ${data} </p>`
  // setTimeout('sendCommand()', 1000);
}
