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
  }

  render () {
    var onOrrOff;

    function getBuffer () {
      axios.post('https://35.178.120.95/getBuffer', {})
      .then(function (response) {
		    onOrOff = response.data.buffer;
        console.log(response);
      })
      .catch(error => console.log(error))
      return onOrOff;
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

    function mainProgram () {
      buffer = false;
      updatePhone();

      (function bufLoop () {
        onOrOff = getBuffer();
        setTimeout(function () {
          if (onOrOff) {
            onTorch();
            bufLoop();
          } else {
            offTorch()
            bufLoop();
          }
        }, 1000);
      })();
    }

    mainProgram();

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">PhoneFlash</h1>
        </header>
        <p>"HOLD UP YOUR FUCKING PHONE"</p>
        <button className='button' onClick={onTorch}>Torch on</button>
        <button className='button' onClick={offTorch}>Torch off</button>
      </div>
    )
  }
}

export default App
