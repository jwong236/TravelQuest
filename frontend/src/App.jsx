import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import './app.css';

function App() {
  return <>
  <div className="homescreen-container" >
    <h1 className="home-title">TravelQuest</h1>
    <p className="home-description">Embark on your quest to travel around the world!</p>
    <TextField className="home-search" id="outlined-basic" label="Enter an Address" variant="outlined"/>
    <form id="image_file" onSubmit={this.handleSubmit}>
      <TextField className = "form-field" type="file"/>
      <Button className = "form-button" variant="contained" color="primary" component="span" type="submit">Upload</Button>
    </form>
  </div>
  </>
}
  
export default App
