// eslint-disable-next-line no-unused-vars
import React from 'react'
// import EvenementA from '../component/EvenementA';
//import 'EvenementA.css'

import { Link } from 'react-router-dom';

function PageEvenement(){
    return(
        <>
            <div className='ctn_evenement'>
                <div className='flex'>
                    <Link to='/creation-event' className='text-xl text-white mb-3 mt-2'>Créer un Evenement</Link>
                </div>
                
            </div>
        </>
    )
}

export default PageEvenement;