 var player = document.getElementById('video');

  var handleSuccess = function(stream) {
    player.srcObject = stream;
  };

  navigator.mediaDevices.getUserMedia({ audio: true, video: true })
      .then(handleSuccess)

 navigator.mediaDevices.enumerateDevices().then((devices) => {
  devices = devices.filter((d) => d.kind === 'videoinput');
});
  navigator.mediaDevices.getUserMedia({
  audio: true,
  video: {
    deviceId: devices[1].deviceId
  }
});