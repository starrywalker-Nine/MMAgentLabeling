import React from'react';
import { Link } from 'react-router-dom'
export default function Plan() {
    return (
        <div className='flex sticky top-[calc(100vh_-_48px-_16px)]
        flex-col h-12 border-t px-2 border-stone-300 justify-end
        text-xs
        '>
            <div className='flex flex-row items-center justify-between'>
                <div>
                    <p className='font-bold'>Enterprise</p>
                    <p className='text-stone-500'>pay as you go</p> 
                </div>
                <Link to='/'>
                    <button className='px-2 py-1.5 font-medium bg-stone-200 hover:bg-stone-300
                    transition-colors rounded
                    '>Log out
                    </button>
                </Link>

            </div>

        </div>
    )

}