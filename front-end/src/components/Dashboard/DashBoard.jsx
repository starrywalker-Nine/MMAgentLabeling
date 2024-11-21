import React from'react';
import TopBar from './TopBar';
import Grid from './Grid';

export default function DashBoard({main}) {
    
    return (
        <div className='bg-white rounded-lg pb-4 shadow h-[100vh]'>
            <TopBar/>
            <div className='h-[85vh]'>
            {main}
            </div>
            {/* <Grid/> */}
        </div>
    )
};
