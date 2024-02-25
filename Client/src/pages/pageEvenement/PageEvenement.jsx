import { BsCalendar2Date, BsCalendar2Event } from "react-icons/bs";
import { IoLocationOutline } from "react-icons/io5";
import { Link } from "react-router-dom";
import airtel from "../../assets/sponsore/Airtel.png";
import logoB from "../../assets/sponsore/logoB.png";
import logoD from "../../assets/sponsore/logoD.jpg";
import orange from "../../assets/sponsore/orangeA.png";
import telma from "../../assets/sponsore/telma.png";
import "./PageEvenement.css";

/*Importation des images*/
//import show from '../../assets/event/eventA.jpg'

export default function PageEvenement() {
  return (
    <>
      <div className="ctn_page_evenement mt-1 mx-auto pt-8 pl-5 pr-5">
        <div className="ctn_title_creer_evenement flex w-full">
          <Link
            to="/creation-event"
            className="btn_creation_event font-medium border-2 w-1/4 py-2 px-12 cursor-pointer text-white font-mono rounded"
          >
            Créer votre propre évènement
          </Link>
        </div>

        <div className="flex mt-8 justify-between flex-wrap">
          <Link to="/single-event">
            <div className="eventeA h-48 bg-white flex">
              <div className="ctn_img_evenement rounded-tl-md"></div>
              <div className="ctn_list_information bg-white">
                <div className="pl-2 mt-1 flex w-full h-6 items-center">
                  <BsCalendar2Event />
                  <h1 className="mb-1 ml-1 mt-2 text-xs">
                    - Evènement : Sport - Nat
                  </h1>
                </div>
                <div className="pl-2 mt-1 flex w-full h-6 items-center">
                  <BsCalendar2Date />
                  <h1 className="mb-1 ml-1 mt-2 text-xs">
                    - Date : 06/08/2024
                  </h1>
                </div>
                <div className="pl-2 mt-1 mb-2 flex w-full h-6 items-center">
                  <IoLocationOutline className="ico_location w-5 h-5" />
                  <h1 className="mb-1 mt-1 text-xs">- Lieu : Itaosy</h1>
                </div>
                <div className="separrateur"></div>

                <div className="ctn_info_plus w-full flex">
                  <div className="ctn_paf w-2/5 h-full flex flex-col">
                    <h1 className="text-xs mt-1 ml-2 underline font-bold">
                      Paf :
                    </h1>
                    <div className="ctn_tarif_chiffre">
                      <p className="text-xs mt-1 ml-2">5000 Ar</p>
                      <p className="text-xs mt-1 ml-2">10000 Ar</p>
                      <p className="text-xs mt-1 ml-2">15000 Ar</p>
                    </div>
                  </div>
                  <div className="ctn_sponsore  w-3/5 h-full">
                    <h1 className="text-xs mt-1 ml-1 underline font-bold mb-1">
                      Sposonrisé par :
                    </h1>
                    <div className="ctn_sponsore ml-1 flex flex-wrap">
                      <img src={airtel} alt="" className="sponse" />
                      <img src={logoB} alt="" className="sponse" />
                      <img src={logoD} alt="" className="sponse" />
                      <img src={telma} alt="" className="sponse" />
                      <img src={orange} alt="" className="sponse" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Link>

          <Link>
            <div className="eventB h-48 bg-white flex">
              <div className="ctn_img_evenementA rounded-tl-md"></div>
              <div className="ctn_list_information bg-white">
                <div className="pl-2 mt-1 flex w-full h-6 items-center">
                  <BsCalendar2Event />
                  <h1 className="mb-1 ml-1 mt-2 text-xs">
                    - Evènement : Mariage
                  </h1>
                </div>
                <div className="pl-2 mt-1 flex w-full h-6 items-center">
                  <BsCalendar2Date />
                  <h1 className="mb-1 ml-1 mt-2 text-xs">
                    - Date : 06/08/2024
                  </h1>
                </div>
                <div className="pl-2 mt-1 mb-2 flex w-full h-6 items-center">
                  <IoLocationOutline className="ico_location w-5 h-5" />
                  <h1 className="mb-1mt-1 text-xs">- Lieu : Ivandry</h1>
                </div>
                <div className="separrateur"></div>

                <div className="ctn_info_plus w-full flex">
                  <div className="ctn_paf w-2/5 h-full flex flex-col">
                    <h1 className="text-xs mt-1 ml-2 underline font-bold">
                      Paf :
                    </h1>
                    <div className="ctn_tarif_chiffre">
                      <p className="text-xs mt-1 ml-2">10000 Ar</p>
                      <p className="text-xs mt-1 ml-2">20000 Ar</p>
                    </div>
                  </div>
                  <div className="ctn_sponsore  w-3/5 h-full">
                    <h1 className="text-xs mt-1 ml-1 underline font-bold mb-1">
                      Sposonrisé par :
                    </h1>
                    <div className="ctn_sponsore ml-1 flex flex-wrap">
                      <img src={telma} alt="" className="sponse" />
                      <img src={orange} alt="" className="sponse" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Link>

          <div className="eventB bg-white h-48 flex">
            <div className="ctn_img_evenementB rounded-tl-md"></div>
            <div className="ctn_list_information bg-white">
              <div className="pl-2 mt-1 flex w-full h-6 items-center">
                <BsCalendar2Event />
                <h1 className="mb-1 ml-1 mt-2 text-xs">
                  - Evènement : Sport - Nat
                </h1>
              </div>
              <div className="pl-2 mt-1 flex w-full h-6 items-center">
                <BsCalendar2Date />
                <h1 className="mb-1 ml-1 mt-2 text-xs">- Date : 06/08/2024</h1>
              </div>
              <div className="pl-2 mt-1 mb-2 flex w-full h-6 items-center">
                <IoLocationOutline className="ico_location w-5 h-5" />
                <h1 className="mb-1 mt-1 text-xs">- Lieu : Itaosy</h1>
              </div>
              <div className="separrateur"></div>

              <div className="ctn_info_plus w-full flex">
                <div className="ctn_paf w-2/5 h-full flex flex-col">
                  <h1 className="text-xs mt-1 ml-2 underline font-bold">
                    Paf :
                  </h1>
                  <div className="ctn_tarif_chiffre">
                    <p className="text-xs mt-1 ml-2">5000 Ar</p>
                    <p className="text-xs mt-1 ml-2">10000 Ar</p>
                  </div>
                </div>
                <div className="ctn_sponsore  w-3/5 h-full">
                  <h1 className="text-xs mt-1 ml-1 underline font-bold mb-1">
                    Sposonrisé par :
                  </h1>
                  <div className="ctn_sponsore ml-1 flex flex-wrap">
                    <img src={airtel} alt="" className="sponse" />
                    <img src={logoB} alt="" className="sponse" />
                    <img src={telma} alt="" className="sponse" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="eventB bg-white h-48 flex mt-3">
            <div className="ctn_img_evenementC rounded-tl-md overlay"></div>
            <div className="ctn_list_information bg-white rounded-lg">
              <div className="pl-2 mt-1 flex w-full h-6 items-center">
                <BsCalendar2Event />
                <h1 className="mb-1 ml-1 mt-2 text-xs">- Evènement : Misse</h1>
              </div>
              <div className="pl-2 mt-1 flex w-full h-6 items-center">
                <BsCalendar2Date />
                <h1 className="mb-1 ml-1 mt-2 text-xs">- Date : 12/14/2024</h1>
              </div>
              <div className="pl-2 mt-1 mb-2 flex w-full h-6 items-center">
                <IoLocationOutline className="ico_location w-5 h-5" />
                <h1 className="mb-1 mt-1 text-xs">- Lieu : Bonara Be</h1>
              </div>
              <div className="separrateur"></div>

              <div className="ctn_info_plus w-full flex">
                <div className="ctn_paf w-2/5 h-full flex flex-col">
                  <h1 className="text-xs mt-1 ml-2 underline font-bold">
                    Paf :
                  </h1>
                  <div className="ctn_tarif_chiffre">
                    <p className="text-xs mt-1 ml-2">25000 Ar</p>
                    <p className="text-xs mt-1 ml-2">30000 Ar</p>
                  </div>
                </div>
                <div className="ctn_sponsore  w-3/5 h-full">
                  <h1 className="text-xs mt-1 ml-1 underline font-bold mb-1">
                    Sposonrisé par :
                  </h1>
                  <div className="ctn_sponsore ml-1 flex flex-wrap">
                    <img src={logoD} alt="" className="sponse" />
                    <img src={telma} alt="" className="sponse" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
