import React, { Component } from 'react'
import './App.css'
import axios from 'axios'
import logo from './heysweetcheeks.png';
//import ImageCapture from './ImageCapture'


class App extends Component {
  constructor () {
    super()
    this.state = {
      username: ''
    }

    this.updatePhone = this.updatePhone.bind(this)
    this.getBuffer = this.getBuffer.bind(this)
    this.ping = this.ping.bind(this)
    this.toggleTorch = this.toggleTorch.bind(this)
  }

  updatePhone () {
    axios.post('http://35.178.120.95/updatePhone', {
      lat: 1,
      longi: 1
    })
    .then(function (response) {
      console.log(response)
    })
    .catch(function (error) {
      console.log(error)
    })
  }

  ping () {
    axios.post('http://35.178.120.95/ping', {})
    .then(response => console.log(response))
    .catch(error => console.log(error))
  }

  getBuffer () {
    axios.post('http://35.178.120.95/getBuffer', {})
    .then(response => console.log(response))
    .catch(error => console.log(error))
  }

  toggleTorch () {
    //Test browser support
    const SUPPORTS_MEDIA_DEVICES = 'mediaDevices' in navigator;

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
            const btn = document.querySelector('.switch');
            btn.addEventListener('click', function(){
              track.applyConstraints({
                advanced: [{torch: true}]
              });
            });
          });
        });
      });

      //The light will be on as long the track exists


    }
  }

  render () {
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
        <button className='button' onClick={this.getBuffer}>Buffer me up daddy</button>
        <button className='button' onClick={this.ping}>Ping me daddy</button>
        <button className='button' onClick={this.toggleTorch}>Flash me daddy</button>
      </div>
      </div>
    )
  }
}

export default App
