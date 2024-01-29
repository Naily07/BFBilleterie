// eslint-disable-next-line no-unused-vars
import React from 'react';
import "../../index.css"

export default function CreationEvenement() {
  return (
    <>
        <div className='ctn_event'>
            <div className='flex justify-between mt-2 mb-2'>
                <h1 className='text-xl'>Création d évènement</h1>
                <input type="text" placeholder='Recherche' className='rounded ctn_input border-solid border-2 border-blue-300 outline-none text-xl'/>
            </div>
            <div className='ctn_element_evenement bg-gray-500 flex justify-between'>
                <div className='ctn_evenement_form flex'>
                    <div className='ctn_image bg-yellow-200 mr-2'>

                    </div>
                    <div className='ctn_information mt-2'>
                        <form>
                            <div className='flex'>
                                <label htmlFor="" className='text-white text-xl'>Evenement :</label>
                                <input type="text" className='ml-2 outline-none border-b-2 bg-transparent w-52 text-white text-xl mb-2'/>
                            </div>
                            <div className='mt-2 text-white'>
                                <label htmlFor="" className='text-xl'>Date   :</label>
                                <input type="date" className='ml-16 outline-none border-b-2 bg-transparent w-52 text-white text-xl mb-2'/>
                            </div>
                            <div className='mt-2 text-white'>
                                <label htmlFor="" className='text-xl'>Lieu    :</label>
                                <input type="text" className='ml-16 outline-none border-b-2 bg-transparent w-52 text-white text-xl mb-2'/>
                            </div>
                        </form>
                        <h1 className='mt-2 text-white text-xl'>Type de billet</h1>
                        <h1 className='mt-2 text-white text-xl mb-2'>Détail</h1>
                        <textarea name="" id="" cols="75" rows="7" className='outline-none'></textarea>
                        <button className='block bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>Publié</button>
                    </div>
                </div>
                <div className='ctn_list_evenement bg-blue-400'>

                </div>
            </div>
        </div>
    </>
  )
}
