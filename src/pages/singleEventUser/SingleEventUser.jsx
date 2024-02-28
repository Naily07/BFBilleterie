// eslint-disable-next-line no-unused-vars
import { motion } from "framer-motion";
import { useState } from "react";
import { BsCalendar2Date, BsCalendar2Event } from "react-icons/bs";
import NumericInput from "react-numeric-input";
import { IoLocationOutline } from "react-icons/io5";
import "./SingleEventUser.css";

import airtel from "../../assets/sponsore/Airtel.png";
import logoB from "../../assets/sponsore/logoB.png";
import logoD from "../../assets/sponsore/logoD.jpg";
import orange from "../../assets/sponsore/orangeA.png";
import telma from "../../assets/sponsore/telma.png";

//import { FaRegPenToSquare } from "react-icons/fa6";
import { Modal } from "../../component/modale/Modal";

import ModalE from "../../component/modalUpdateEvenent/ModaleEvent";

export default function SingleEventUser() {
  const [isAnimation, setIsAnimation] = useState(false);
  const [openModal, setOpenModal] = useState(false);

  return (
    <>
      <div className="ctn_single_evenement h-screen">
        <div className="ctn_presentation_evenement bg-white">
          <motion.div
            className="ctn_pict bg-yellow-200 "
            animate={{
              //x: isAnimating ? 600 : 0,
              opacity: isAnimation ? 1 : 0.8,
              //rotate: isAnimating ? 360 : 0
              height: isAnimation ? "100%" : "35%",
            }}
            onClick={() => {
              setIsAnimation(!isAnimation);
            }}
          ></motion.div>

          <motion.div
            className="ctn_information_evenement flex justify-center"
            animate={{
              opacity: isAnimation ? 0.0 : 1,
            }}
          >
            <div className="ctn_info_paf">
              <form className="mt-3">
                <div className="flex">
                  <BsCalendar2Event className="mt-1 font-bold" />
                  <label
                    htmlFor=""
                    className="text-black text-gl ml-1 font-semibold"
                  >
                    - Evenement :
                  </label>
                  <h1 className="text-lg ml-2">Miss and Mister</h1>
                </div>
                <div className="mt-2 text-black flex">
                  <BsCalendar2Date className="mt-1" />
                  <label htmlFor="" className="text-gl ml-1 font-semibold">
                    - Date :
                  </label>
                  <div className="ctn_info_date_single flex items-center">
                    <h1 className="text-lg ml-14">26/03/2024</h1>
                    <h1 className="debut ml-4">
                      <span className="font-bold">à :</span> 17:30 -{" "}
                    </h1>
                    <h1 className="fin ml-1">23:00</h1>
                  </div>
                </div>
                <div className="ctn_info_lieu mt-2 text-black flex">
                  <IoLocationOutline className="icon_lieu" />
                  <label htmlFor="" className="text-gl font-semibold">
                    - Lieu :
                  </label>
                  <h1 className="text-lg ml-14">Ambatondrazaka</h1>
                </div>
              </form>

              <div className="ctn_info_paf border-t-2 border-gray-500 pt-2 flex">
                <h1 className="font-semibold">Paf:</h1>
                <div className="ctn_tarif_chiffre">
                  <div className="ctn_paf flex justify-around items-center">
                    <p className="text-lg ml-2">5000 Ar</p>
                    <p className="">- Simple -</p>
                  </div>
                  <div className="ctn_paf flex justify-around items-center">
                    <p className="text-lg ml-2">6000 Ar</p>
                    <p>- Silver -</p>
                  </div>
                  <div className="ctn_paf flex justify-around items-center">
                    <p className="text-lg ml-2">12000 Ar</p>
                    <p>- Gold -</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="ctn_detail_singleEvente ml-12 pl-4 border-l-2 border-zinc-600 w-2/4 z-1">
              <h1 className="mt-2 text-black text-lg mb-1 font-bold">
                Sponsorisé par
              </h1>
              <div className="separateur_single w-14 h-2 bg-arapawa-800 mb-2"></div>
              <div className="ctn_sponsore flex flex-wrap mt-5">
                <img src={airtel} alt="" className="sponse_single_event" />
                <img src={logoB} alt="" className="sponse_single_event" />
                <img src={logoD} alt="" className="sponse_single_event" />
                <img src={telma} alt="" className="sponse_single_event" />
                <img src={orange} alt="" className="sponse_single_event" />
              </div>
            </div>

            {
              //<FaRegPenToSquare
              //className="iconSquar_info_single mr-2 mb-2 w-6 h-6"
              //onClick={() => {
              //setOpenModal(true);
              //}}
              ///>
            }

            <div className="ctn_modale">
              <ModalE className="modalplace" />
            </div>
          </motion.div>
        </div>

        {openModal && <Modal closeModal={setOpenModal} />}

        <section className="ctn_achat_billet mx-auto mt-5 mb-5">
          <div className="ctn_type_mode_payment flex px-2 flex-wrap items-center mx-auto justify-between border border-gray-300 pt-4 pb-3">
            <div className="ctn_radio_btn">
              <h1 className="pl-6 mt-3 text-lg font-bold shadow-md pb-3 text-arapawa-800">
                Type de billet
              </h1>
              <div className="ctn_radio px-2 mt-4">
                <div className="ctn_simple mt-3 mb-2">
                  <label htmlFor="" className="text-lg ml-3">
                    - Simple
                  </label>
                  <input type="checkbox" className="ml-7" />
                  <NumericInput className="w-20 ml-9 focus:outline-none focus:bg-white focus:border-gray-500" />
                </div>
                <div className="ctn_silver mt-3">
                  <label htmlFor="" className="text-lg ml-3">
                    - Silver
                  </label>
                  <input type="checkbox" className="ml-10" />
                  <NumericInput className="w-20 ml-9 focus:outline-none focus:bg-white focus:border-gray-500" />
                </div>
                <div className="ctn_gold mt-3">
                  <label htmlFor="" className="text-lg ml-3">
                    - Gold
                  </label>
                  <input type="checkbox" className="ml-11" />
                  <NumericInput className="w-20 ml-9 focus:outline-none focus:bg-white focus:border-gray-500" />
                </div>
              </div>
            </div>
            <div className="ctn_mode_payment">
              <h1 className="pl-6 mt-3 text-lg font-bold shadow-md pb-3 text-arapawa-800">
                Mode de payement
              </h1>

              <select
                name=""
                className="ml-6 font-bold mt-4 block appearance-none w-3/4 bg-white border border-gray-500 hover:border-gray-700 px-4 py-2 pr-4 rounded focus:outline-none focus:shadow-outline"
              >
                <option value="" className="">
                  MVola
                </option>
                <option value="">Orange Money</option>
                <option value="">Airtel Money</option>
              </select>
            </div>
            <button className="bg-arapawa-800 text-white px-4 py-2 font-bolb rounded mt-3 ml-1 hover:bg-arapawa-700">
              Confirmer
            </button>
          </div>
        </section>
        <div className="w-full h-2"></div>
      </div>
    </>
  );
}
