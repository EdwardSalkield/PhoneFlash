import React, { Component } from 'react'
import './App.css'
import axios from 'axios'
import logo from './heysweetcheeks.png';

class App extends Component {

  constructor () {
    super()
    this.state = {
      username: ''
    }
    this.updatePhone = this.updatePhone.bind(this)
    //this.getBuffer = this.getBuffer.bind(this)
    //this.onTorch = this.onTorch.bind(this)
    //this.offTorch = this.offTorch.bind(this)
  }

  updatePhone () {
    var latit;
    var longit;
    navigator.geolocation.getCurrentPosition(function(location) {
      latit = location.coords.latitude;
      longit = location.coords.longitude;
      console.log(location.coords.latitude);
      console.log(location.coords.longitude);
      //console.log(Math.round((new Date()).getTime() / 1000));
      console.log(new Date().getTime()/1000);
      console.log(Date.now());
      //console.log(location.coords.accuracy);
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





  render () {
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

    function getBuffer () {
      var beforeTime = new Date().getTime()/1000;
      var afterTime;
      var myPing;
      axios.post('https://35.178.120.95/getBuffer', {})
      .then(function (response) {
        console.log(response);
        afterTime = new Date().getTime()/1000;
        myPing = (afterTime-beforeTime)/2 + 100;
        // console.log("Before Time: ", beforeTime);
        // console.log("After Time: ", afterTime);
        // console.log("Ping: ", myPing);
        while (new Date().getTime()/1000 < response.data.nextUpdateAt.toFixed(3)+100){}
        //console.log("NEXT GETBUFFER");
      })
      .catch(error => console.log(error))
    }

    function mainProgram () {
    	//var timeToWait = 1000;
      //var ping = getPing();
      //console.log(ping);

      (function theLoop () {
        setTimeout(function () {
          getBuffer();
          onTorch();
          offTorch();
          //console.log(ping);

          // Start looped code
          //
          // Call getBuffer
          // update timeToWait
          // store the buffer
  				//this.getBuffer;
          //console.log("Hey");
  				//timeToWait =

  				// End looped code
          theLoop();
        //}, timeToWait);
      });
      })();

    }
    //this.forceUpdate();

    mainProgram();

    return (
      <div className="Big-Container">
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">PhoneFlash</h1>
        </header>
      </div>
        <div className='button__container'>
          <button className='button' onClick={this.updatePhone}>L0cate me daddy</button>


        </div>
      </div>
    )
  }
}

export default App
