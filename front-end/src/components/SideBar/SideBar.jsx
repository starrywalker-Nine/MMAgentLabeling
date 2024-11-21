import React from'react';
import AccountToggle from './AccountToggle';
import Search from './Search';
import SidebarWithSearch from './SideBar2';
import RouteSelect from './RouteSelect';
import Plan from './Plan';
import { useState } from 'react';

export default function SideBar({selectedIndex, handleButtonClick}) {

    return (
        <div>
            <div className='overflow-y-scroll sticky top-4 h-[calc(100vh-32px-48px)]'>
                {/* Main content of SideBar */}
                <AccountToggle />
                <Search />
                <RouteSelect selectedIndex={selectedIndex} handleButtonClick={handleButtonClick} />
                {/* <SidebarWithSearch /> */}
            </div>
            <Plan />
        </div>
    )
};
