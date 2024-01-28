import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import HomeIcon from '@mui/icons-material/Home';
import './app.css';

function test() {
  console.log("Hello");
  fetch("http://localhost:5000")
  .then(res => res.json())
  .then(resp => {console.log(resp)});
}

function App() {
  return <>
    <div className="homescreen-container" >
      <h1 className="home-title">TravelQuest</h1>
      <p className="home-description">Embark on your quest to travel around the world!</p>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: '24px' }}>
        <HomeIcon fontSize='large' />
        <TextField className="home-search" id="outlined-basic" label="Address" variant="outlined" InputLabelProps={{ style: { color: 'white' } }} sx={{
          fieldset: { borderColor: "white" }

        }} />
      </Box>
      <form id="image_file">
        <TextField className="form-field" type="file" InputLabelProps={{ style: { color: 'white' } }} sx={{
          fieldset: { borderColor: "white" }
        }} />
        <Button className="form-button" variant="contained" color="primary" component="span" type="submit" onClick={test}>Upload</Button>
    </form>
  </div >
  </>
}

export default App
