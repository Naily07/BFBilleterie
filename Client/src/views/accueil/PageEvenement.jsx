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
                    <Link to='/creation-event' className='text-xl text-white mb-3 mt-2'>Créer un Evenement</Link>
                </div>
                <div className='flex justify-center'>
                    <div className='flex'>
                        {/* <EvenementA /> */}
                    </div>
                    <div className='eventB bg-white h-48 flex'>                      
                        <div className='ctn_img_evenement bg-yellow-200'></div>
                        <div className='ctn_list_information mt-2 ml-1'>
                            <h1 className='mb-1'>Evènement : Smatching</h1>
                            <h1 className='mb-1'>Date : 12/03/2024</h1>
                            <h1 className='mb-1'>Lieu : Ankadidramamy</h1>
                            <div className='separrateur'></div>
                        </div>
                    </div>

                    <div className='eventB bg-white h-48 flex'>
                        <div className='ctn_img_evenement bg-yellow-200'></div>
                            <div className='ctn_list_information mt-2 ml-1'>
                                <h1 className='mb-1'>Evènement : Smatching</h1>
                                <h1 className='mb-1'>Date : 12/03/2024</h1>
                                <h1 className='mb-1'>Lieu : Ankadidramamy</h1>
                            <div className='separrateur'></div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default PageEvenement;