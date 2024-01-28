import Grid from '@mui/material/Grid';
import React, { useState } from 'react';
import './results.css'

export default function Results() {
    
    console.log("hello");
    return <>
        <Grid className="grid-container" container spacing={2}>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
            <Grid>
                <div className ="grid-small-container">
                    <div className ="item">Item 1</div>
                </div>
            </Grid>
        </Grid>
    
    </>
}