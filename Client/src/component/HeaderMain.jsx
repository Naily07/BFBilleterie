// eslint-disable-next-line no-unused-vars
import React from 'react'
import { Link } from 'react-router-dom';

export default function Header(){
    return(
        <>
            <div className='ctn_nav h-12 bg-white flex justify-between items-center mb-1 shadow-lg'>
                <h1 className='c_logo text-green-600 text-2xl'>Logo</h1>
                <nav>
                    <ul className='flex'>                      
                        <li className='text-black text-xl hover:text-blue-700'>
                            <Link to='/'>Evènements</Link>
                        </li>
                        <li className='ml-8 text-black text-xl hover:text-blue-700'><a href="#">Point de vente</a></li>
                        <li className='ml-8 text-black text-xl hover:text-blue-700'><a href="#">Compte</a></li>
                    </ul>
                </nav>
            </div>
        </> 
    )
}

