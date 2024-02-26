// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react'
import './SingleEvent.css'
import { motion } from 'framer-motion'
import { BsCalendar2Event } from "react-icons/bs";
import { BsCalendar2Date } from "react-icons/bs";
import { IoLocationOutline } from "react-icons/io5";

import airtel from '../../assets/sponsore/Airtel.png'
import logoB from '../../assets/sponsore/logoB.png'
import logoD from '../../assets/sponsore/logoD.jpg'
import telma from '../../assets/sponsore/telma.png'
import orange from '../../assets/sponsore/orangeA.png'

import { FaRegPenToSquare } from "react-icons/fa6";
import { Modal } from '../../component/modale/Modal';

export default function SingleEvent() {

  const [isAnimation, setIsAnimation] = useState(false) 
  const [openModal, setOpenModal] = useState(false) 

  return (
    <>
      <div className="ctn_single_evenement h-screen">
        <div className="ctn_presentation_evenement bg-white">

          <motion.div className="ctn_pict bg-yellow-200 "
            animate={{
              //x: isAnimating ? 600 : 0,
              opacity: isAnimation ? 1 : 0.8,
              //rotate: isAnimating ? 360 : 0
              height: isAnimation ? "100%" : "35%",
          }}
            onClick={()=>{setIsAnimation(!isAnimation)}}
          >
          </motion.div>

          <motion.div className="ctn_information_evenement flex justify-center"
            animate={{
              opacity: isAnimation ? .00 : 1,
            }}
          >

            <div className="ctn_info_paf">
              <form className='mt-3'>
                <div className='flex'>
                  <BsCalendar2Event className='mt-1 font-bold'/>
                  <label htmlFor="" className='text-black text-gl ml-1 font-semibold'>- Evenement :</label>
                  <h1 className='text-lg ml-2'>Miss and Mister</h1>
                </div>
                <div className='mt-2 text-black flex'>
                  <BsCalendar2Date  className='mt-1'/>
                  <label htmlFor="" className='text-gl ml-1 font-semibold'>- Date   :</label>
                  <div className="ctn_info_date_single flex items-center">
                    <h1 className='text-lg ml-14'>26/03/2024</h1>
                    <h1 className='debut ml-4'><span className='font-bold'>à :</span> 17:30 - </h1>
                    <h1 className='fin ml-1'>23:00</h1>
                  </div>
                </div>
                <div className='ctn_info_lieu mt-2 text-black flex'>
                  <IoLocationOutline  className='icon_lieu'/>
                  <label htmlFor="" className='text-gl font-semibold'>- Lieu    :</label>
                  <h1 className='text-lg ml-14'>Ambatondrazaka</h1>
                </div>  
              </form>

              <div className="ctn_info_paf border-t-2 border-gray-500 pt-2 flex">
                <h1 className='font-semibold'>Paf:</h1>
                <div className='ctn_tarif_chiffre'>

                    <div className="ctn_paf flex justify-around items-center">
                      <p className='text-lg ml-2'>5000 Ar</p>
                      <p className=''>- Simple -</p>
                    </div>
                    <div className="ctn_paf flex justify-around items-center">
                      <p className='text-lg ml-2'>6000 Ar</p>
                      <p>- Silver -</p>
                    </div>
                    <div className="ctn_paf flex justify-around items-center">
                      <p className='text-lg ml-2'>12000 Ar</p>
                      <p>- Gold -</p>
                    </div>

                </div>
              </div>
            </div>

            <div className="ctn_detail_singleEvente ml-12 pl-4 border-l-2 border-zinc-600 w-2/4 z-1">
                <h1 className='mt-2 text-black text-lg mb-1 font-bold'>Sponsorisé par</h1>
                <div className="separateur_single w-14 h-2 bg-arapawa-800 mb-2"></div>
                <div className="ctn_sponsore flex flex-wrap mt-5">
                    <img src={ airtel } alt="" className='sponse_single_event'/>
                    <img src={ logoB } alt="" className='sponse_single_event'/>
                    <img src={ logoD } alt="" className='sponse_single_event'/>
                    <img src={ telma } alt="" className='sponse_single_event'/>
                    <img src={ orange } alt="" className='sponse_single_event'/>
                </div>
            </div>
          
            <FaRegPenToSquare className='iconSquar_info_single mr-2 mb-2 w-6 h-6' 
            onClick={() => { 
              setOpenModal(true);        
              }}
            />  

          </motion.div>
        </div>

        { openModal && <Modal closeModal={ setOpenModal }/> }

        <div className="ctn_table flex justify-center items-center mt-9">
          <table className="table-auto text-black border-2">
            <thead>
              <tr>
                <th className="bgz_type px-4 py-2 text-white">Type de billet</th>
                <th className="bgz_s    border px-16 py-2 text-white">Simple</th>
                <th className="bgz_si   border px-16 py-2 text-white">Silver</th>
                <th className="bgz_g    border px-16 py-2 text-white">Gold</th>
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
