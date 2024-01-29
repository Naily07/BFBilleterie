// eslint-disable-next-line no-unused-vars
import React from 'react'
import './EvenementA.css'

import { Link } from 'react-router-dom'

export default function EvenementA() {
  return (
    <>
        <div className='ctn_evenemenets'>

            <Link to='/'>
                <div className='eventeA w-1/3 h-48 bg-red-300'>
                    <h1 className='text-xl'>Test Evenement modification</h1>
                </div>
            </Link>

        </div>
    </>
  )
}
