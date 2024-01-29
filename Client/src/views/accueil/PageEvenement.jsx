// eslint-disable-next-line no-unused-vars
import React from 'react'
import EvenementA from '../../component/EvenementA';
import "../../index.css"

//import 'EvenementA.css'

import { Link } from 'react-router-dom';

function PageNavigation(){
    return(
        <>
            <div className='ctn_evenement bg-yellow-300'>
                <div className='flex'>
                    <Link to='/' className='text-xl underline mb-3 mt-2'>Créer un Evènement</Link>
                </div>
                <EvenementA />
            </div>
        </>
    )
}

export default PageNavigation;