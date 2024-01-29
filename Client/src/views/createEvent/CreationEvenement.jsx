// eslint-disable-next-line no-unused-vars
import React from 'react';
import './CreationEvenement.css'
//import List_Event from '../component/List_Event';
import './CreationEvenement.css'

export default function CreationEvenement() {
  return (
    <>
        <div className='ctn_event'>
            <div className='flex justify-between mt-4 mb-4 ml-40'>
                <h1 className='text-xl text-white underlin'>Création d évènement</h1>
            </div>

            <div className='ctn_element_evenement flex justify-center h-full'>
                <div className='ctn_evenement_form bg-zinc-300 flex'>
                    <div className='ctn_image bg-yellow-200 mr-2'>

                    </div>
                    <div className='ctn_information mt-2'>
                        <form>
                            <div className='flex'>
                                <label htmlFor="" className='text-black text-xl'>Evenement  :</label>
                                <input type="text" className='ml-2 outline-none border-b-2 border-black bg-transparent w-52 text-black text-xl mb-2'/>
                            </div>
                            <div className='mt-2 text-black'>
                                <label htmlFor="" className='text-xl'>Date   :</label>
                                <input type="date" className='ml-16 outline-none border-b-2 border-black bg-transparent w-52 text-black text-xl mb-2'/>
                            </div>
                            <div className='mt-2 text-black mb-3'>
                                <label htmlFor="" className='text-xl'>Lieu    :</label>
                                <input type="text" className='ml-16 outline-none border-b-2 border-black bg-transparent w-52 text-black text-xl mb-3'/>
                            </div>
                        </form>

                            <div className='mb-3'>
                                <table className="table-auto text-black border-2 border-black">
                                    <thead>
                                    <tr>
                                        <th className="px-3 py-2">Type de billet</th>
                                        <th className="border border-black px-8 py-2">Simple</th>
                                        <th className="border border-black px-8 py-2">Silver</th>
                                        <th className="border border-black px-8 py-2">Gold</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td className="border border-black px-8 py-2">Nombre de disponible</td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                    </tr>
                                    <tr className="">
                                        <td className="border border-black px-8 py-2">Arhive</td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20'/></td>
                                    </tr>
                                    <tr>
                                        <td className="border border-black px-8 py-2">Totale</td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20' disabled/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20' disabled/></td>
                                        <td className="ctn_inp border border-black px-8 py-2"><input type="text" className='ctn-input outline-none bg-transparent w-20' disabled/></td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                        <h1 className='mt-2 text-black text-xl mb-3'>Détail</h1>
                        <textarea name="" id="" cols="73" rows="7" className='outline-none mb-2'></textarea>
                        <button className='block bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4'>Publiée</button>
                    </div>
                </div>       
            </div>
            <div className='ctn_foot'>

            </div>
        </div>
    </>
  )
}
