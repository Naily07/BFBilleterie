import { Link } from "react-router-dom";
import "./Navigation.css";
import { FaCircleUser } from "react-icons/fa6";
import { SiHomeassistantcommunitystore } from "react-icons/si";
import { SlMenu } from "react-icons/sl";
import { TbCalendarEvent } from "react-icons/tb";
import { IoHomeOutline } from "react-icons/io5";

export default function Header() {
  return (
    <>
      <div className="ctn_menu flex justify-between items-center pl-10 pr-10 pt-4 pb-4 shadow-md">
        <h1 className="text-white text-2xl font-semibold">Logo B</h1>
        <ul className="ctn_menu_navigation_ul flex">
          <li className="ml-10 text-white text-lg hover:text-gray-300">
            <Link to="/accueil">
              <IoHomeOutline className="ico_home inline mr-1" />
              Accueil
            </Link>
          </li>
          <li className="ml-10 text-white text-lg hover:text-gray-300">
            <Link to="/page-evenement">
              <TbCalendarEvent className="ico_event inline mr-1" />
              Evènements
            </Link>
          </li>
          <li className="ml-10 text-white text-lg hover:text-gray-300">
            <Link to="/point-de-vente">
              <SiHomeassistantcommunitystore className="ico_sale inline mr-1" />
              Point de vente
            </Link>
          </li>
          <li className="ml-10 text-white text-lg hover:text-gray-300">
            <Link>
              <FaCircleUser className="ico_user inline mr-1" />
              <span className="test_responsive">Mon Compte</span>
            </Link>
          </li>
        </ul>
        <div className="ctn_icone_menu mt-2 ">
          <SlMenu className="text-white w-6 h-6 cursor-pointer" />
        </div>
        <div className="ctn_menu_responsive_manaraka"></div>
      </div>
      <div className="separation"></div>
    </>
  );
}
