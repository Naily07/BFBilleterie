// eslint-disable-next-line no-unused-vars
import React from 'react'
// import EvenementA from '../component/EvenementA';
//import 'EvenementA.css'

import { Link } from 'react-router-dom';

function PageEvenement(){
    return(
        <>
            <div className='ctn_evenement h-screen'>
                <div className='flex'>
                    <Link to='/' className='text-xl underline mb-3 mt-2'>Créer un Evènement</Link>
                </div>
            </div>
        </>
    )
}

export default PageEvenement;