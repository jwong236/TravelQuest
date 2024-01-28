import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import HomeIcon from '@mui/icons-material/Home';
import { Link } from 'react-router-dom';
import './app.css';

function test() {
  let data = {"address": document.getElementById("address").value};
  console.log(data);
  console.log(JSON.stringify(data));
  console.log(data["address"]);
  fetch("http://127.0.0.1:5000/", {
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "body": JSON.stringify(data),
  })
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
        <TextField className="home-search" id="address" label="Address" variant="outlined" InputLabelProps={{ style: { color: 'white' } }} sx={{fieldset: { borderColor: "white" },"&:hover fieldset": {borderColor: "white"} ,input: {color: "white"}}} />
        <Link to={'results'}>
          <Button className="form-button" variant="contained" color="primary" component="span" type="submit" onClick={test}>Search</Button>
        </Link>
      </Box>
      <form id="image_file">
        <TextField className="form-field" type="file" InputLabelProps={{ style: { color: 'white' } }} sx={{fieldset: { borderColor: "white" },input: {color: "white", fontWeight:'700'}}} />
        <Button className="form-button" variant="contained" color="primary" component="span" type="submit" onClick={test}>Upload</Button>
    </form>
  </div >
  </>
}

export default App
