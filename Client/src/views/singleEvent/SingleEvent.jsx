// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react'
import './SingleEvent.css'
import { motion } from 'framer-motion'

export default function SingleEvent() {

  const [isAnimation, setIsAnimation] = useState(false) 

  return (
    <>
      <div className="ctn_single_evenement h-screen">
        <div className="ctn_presentation_evenement bg-zinc-300">

          <motion.div className="ctn_pict bg-yellow-200 "
            animate={{
              //x: isAnimating ? 600 : 0,
              opacity: isAnimation ? 1 : 0.5,
              //rotate: isAnimating ? 360 : 0
              height: isAnimation ? "100%" : "35%",
          }}
            onClick={()=>{setIsAnimation(!isAnimation)}}
          >
            Picturee
          </motion.div>

          <motion.div className="ctn_information_evenement flex justify-center"
            animate={{
              opacity: isAnimation ? 0 : 1,
            }}
            onClick={()=>{setIsAnimation(!isAnimation)}}
          >
            <form className='mt-3'>
              <div className='flex'>
                  <label htmlFor="" className='text-black text-xl'>Evenement :</label>
                  <h1 className='text-xl ml-2'>Miss and Mister</h1>
              </div>
              <div className='mt-2 text-black flex'>
                  <label htmlFor="" className='text-xl'>Date   :</label>
                  <h1 className='text-xl ml-16'>26/02/2024</h1>
              </div>
              <div className='mt-2 text-black flex'>
                  <label htmlFor="" className='text-xl'>Lieu    :</label>
                  <h1 className='text-xl ml-16'>Ambatondrazaka</h1>
              </div>  
            </form>
            <div className="ctn_detail_singleEvente ml-12 pl-4 border-l-2 border-zinc-600 w-2/4">
                <h1 className='mt-2 text-black text-xl mb-2 underline'>Détail</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi assumenda nulla numquam excepturi commodi a suscipit, praesentium nemo minima? Eaque.</p>
            </div>
          </motion.div>          
        </div>

        <div className="ctn_table flex justify-center items-center mt-9">
          <table className="table-auto text-white">
            <thead>
              <tr>
                <th className="px-4 py-2"></th>
                <th className="border px-16 py-2">Simple</th>
                <th className="border px-16 py-2">Silver</th>
                <th className="border px-16 py-2">Gold</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border px-16 py-2">Nombre de disponible</td>
                <td className="border px-16 py-2">122</td>
                <td className="border px-16 py-2">858</td>
                <td className="border px-16 py-2">858</td>
              </tr>
              <tr className="">
                <td className="border px-16 py-2">Arhive</td>
                <td className="border px-16 py-2">457</td>
                <td className="border px-16 py-2">112</td>
                <td className="border px-16 py-2">112</td>
              </tr>
              <tr>
                <td className="border px-16 py-2">Total</td>
                <td className="border px-16 py-2">45</td>
                <td className="border px-16 py-2">112</td>
                <td className="border px-16 py-2">166</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </>
  )
}
