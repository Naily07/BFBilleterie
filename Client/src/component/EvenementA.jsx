// eslint-disable-next-line no-unused-vars
import React from 'react'
import './EvenementA.css'

import { Link } from 'react-router-dom'

export default function EvenementA() {
  return (
    <>
        <div className='ctn_evenemenets'>

          <Link to='/single-event'>
              <div className='eventeA h-48 bg-white flex'>
                  <div className='ctn_img_evenement bg-yellow-200'></div>
                    <div className='ctn_list_information mt-2 ml-1'>
                        <h1 className='mb-1'>Evènement : Sport6Nat</h1>
                        <h1 className='mb-1'>Date : 06/08/2024</h1>
                        <h1 className='mb-1'>Lieu : Itaosy</h1>
                    <div className='separrateur'></div>
                  </div>
              </div>
          </Link>
        </div>
    </>
  )
}
