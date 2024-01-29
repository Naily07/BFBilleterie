import "../../index.css"
export default function SingleEvent() {
  return (
    <>
      <div className="ctn_single_evenement h-screen bg-yellow-300">
        <div className="ctn_presentation_evenement bg-gray-300">
          <div className="ctn_pict bg-yellow-200  ">Picturee</div>

          <div className="ctn_information_evenement flex">
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
            <div className="h-full bg-red-600 w-2/4">
                <h1 className='mt-2 text-white text-xl mb-2'>Détail</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi assumenda nulla numquam excepturi commodi a suscipit, praesentium nemo minima? Eaque.</p>
            </div>

          </div>
        </div>
        <div>
          <h1 className="text-xl text-white">Table principale Application</h1>
        </div>
      </div>
    </>
  )
}
