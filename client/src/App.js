import React, { Component } from 'react'
import './App.css'
import axios from 'axios'
import logo from './flashinglight.png';

class App extends Component {

  constructor () {
    super()
    this.state = {
      username: ''
    }
    //this.updatePhone = this.updatePhone.bind(this)
    //this.mainProgram = this.mainProgram.bind(this)
  }



  render () {
    var buffer = [];
    var myPing;

    function getBuffer () {
      var afterTime;
      var servertime;
      var beforeTime = new Date().getTime()/1000;
      axios.post('https://35.178.120.95/getBuffer', {})
      .then(function (response) {
		    // Update the buffer
		    buffer = response.data.buffer;
        servertime = response.data.curenttime;
        console.log(response);
      })
      .catch(error => console.log(error))
      afterTime = new Date().getTime()/1000;
      myPing = afterTime - servertime + (afterTime-beforeTime)/2 + 100; // REMOVE THIS 100 AT SOME POINT
      return myPing;
    };
    function onTorch () {
      //Test browser support
      const SUPPORTS_MEDIA_DEVICES = 'mediaDevices' in navigator;
      let ImageCapture = window.ImageCapture;
      if (SUPPORTS_MEDIA_DEVICES) {
      //Get the environment camera (usually the second one)
        navigator.mediaDevices.enumerateDevices().then(devices => {
          const cameras = devices.filter((device) => device.kind === 'videoinput');
          if (cameras.length === 0) {
            throw 'No camera found on this device.';
          }
          const camera = cameras[cameras.length - 1];
          // Create stream and get video track
          navigator.mediaDevices.getUserMedia({
            video: {
              deviceId: camera.deviceId,
              facingMode: ['user', 'environment'],
              height: {ideal: 1080},
              width: {ideal: 1920}
            }
          }).then(stream => {
            const track = stream.getVideoTracks()[0];
            //Create image capture object and get camera capabilities
            const imageCapture = new ImageCapture(track)
            const photoCapabilities = imageCapture.getPhotoCapabilities().then(() => {
              //todo: check if camera has a torch
              //let there be light!
              track.applyConstraints({
                advanced: [{torch: true}]

              })
              // const btn = document.querySelector('.switch');
              // btn.addEventListener('click', function(){
              //   track.applyConstraints({
              //     advanced: [{torch: true}]
              //   });
              // });
            });
          });
        });
      //The light will be on as long the track exists
      }
    }
    function offTorch () {
      //Test browser support
      const SUPPORTS_MEDIA_DEVICES = 'mediaDevices' in navigator;
      let ImageCapture = window.ImageCapture;
      if (SUPPORTS_MEDIA_DEVICES) {
      //Get the environment camera (usually the second one)
        navigator.mediaDevices.enumerateDevices().then(devices => {
          const cameras = devices.filter((device) => device.kind === 'videoinput');
          if (cameras.length === 0) {
            throw 'No camera found on this device.';
          }
          const camera = cameras[cameras.length - 1];
          // Create stream and get video track
          navigator.mediaDevices.getUserMedia({
            video: {
              deviceId: camera.deviceId,
              facingMode: ['user', 'environment'],
              height: {ideal: 1080},
              width: {ideal: 1920}
            }
          }).then(stream => {
            const track = stream.getVideoTracks()[0];
            //Create image capture object and get camera capabilities
            const imageCapture = new ImageCapture(track)
            const photoCapabilities = imageCapture.getPhotoCapabilities().then(() => {
              //todo: check if camera has a torch
              //let there be light!
              track.applyConstraints({
                advanced: [{torch: false}]

              })
              // const btn = document.querySelector('.switch');
              // btn.addEventListener('click', function(){
              //   track.applyConstraints({
              //     advanced: [{torch: false}]
              //   });
              // });
            });
          });
        });
      //The light will be on as long the track exists
      }
    }
    function updatePhone () {
      var latit;
      var longit;
      navigator.geolocation.getCurrentPosition(function(location) {
        latit = location.coords.latitude;
        longit = location.coords.longitude;
      });
      axios.post('https://35.178.120.95/updatePhone', {
        lat: latit,
        longi: longit
      })
      .then(function (response) {
        console.log(response)
      })
      .catch(function (error) {
        console.log(error)
      })
    }

    function mainProgram () {
      updatePhone();
      myPing = getBuffer();
		  // Iterate over buffer, and output the song
  		for (var i = 0; i < buffer.length; i++) {
        if (buffer[i][1] === "on") {
          while (new Date().getTime()/1000 < buffer[i][0]+myPing) {}
          onTorch();
        } else if (buffer[i][1] === "off") {
          while (new Date().getTime()/1000 < buffer[i][0]+myPing) {}
          offTorch();
        }
      }
  			// if ((new Date().getTime()/1000 - myPing) > buffer[i][0]) {
  			// 	if (buffer[i][1] == "on")  {
  			// 		onTorch();
  			// 	} else if (buffer[i][1] == "off") {
  			// 		offTorch();
  			// 	}
  				//i+=1;
  			//}
      // (function theLoop () {
      //   setTimeout(function () {
      //
      //     getBuffer();
      //     onTorch();
      //     offTorch();
      //     theLoop();
      //   });
      // })();
    }

    mainProgram();

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">PhoneFlash</h1>
        </header>
        <p>"HOLD UP YOUR FUCKING PHONE"</p>
      </div>
    )
  }
}

export default App
