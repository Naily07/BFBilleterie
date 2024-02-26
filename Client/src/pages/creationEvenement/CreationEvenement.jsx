import { useRef, useState } from "react";
import "./CreationEvenement.css";
//import { FaSquarePen } from "react-icons/fa6";
import { FaRegPenToSquare } from "react-icons/fa6";
//import { FaLocationDot } from "react-icons/fa6";
import { BsTicketPerforated } from "react-icons/bs";
import { FaPlus, FaRegImage } from "react-icons/fa6";
import { IoLocationOutline } from "react-icons/io5";
import { MdOutlineDateRange } from "react-icons/md";

//import dowload from "../../assets/sponsore/dowload.png";

export default function CreationEvenement() {
  const [isShow, setIsShow] = useState(false);
  const [isShowChoix, setIsShowChoix] = useState(false);
  const inputref = useRef(null);
  const [image, setImage] = useState("");
  const [choixImage, setChoixImage] = useState([]);
  const inputRefLogo = useRef(null);

  const selectImage = (event) => {
    //event.preventDefault();
    const files = Array.from(event.target.files);
    setChoixImage(files);
  };

  const handleClickLogo = () => {
    inputRefLogo.current.click();
  };

  const handleImageClick = () => {
    inputref.current.click();
  };
  const handleImageChange = (event) => {
    //const file = event.target.files[0];
    //console.log(file);
    setImage(event.target.files[0]);
  };

  const handleRemoveLogo = (id) => {
    // Supprime l'image du tableau en utilisant son identifiant
    const newChoixImage = choixImage.filter((file, index) =>
      file.id ? file.id !== id : index !== id
    );
    // Met à jour le tableau d'images
    setChoixImage(newChoixImage);
  };

  return (
    <>
      <div className="ctn_creation_evenement bg-white mx-auto pt-5 pl-5 pr-5">
        <h1 className="text-md font-medium uppercase ">
          Créer votre évènement
        </h1>
        <div className="ctn_information mb-5">
          <div className="shadow-md flex pb-3 mb-4">
            <FaRegPenToSquare className="iconSquar_info ml-2 mt-1" />
            <div>
              <h1 className="font-bold ml-2 mt-1 text-arapawa-800">
                Informations
              </h1>
              <p className="opacity-50 ml-3">
                Rempliser les informations de base
              </p>
            </div>
          </div>

          <input
            type="text"
            placeholder="Nom de l'évènement"
            className='appearance-none block w-full text-gray-700 border border-gray-500 hover:border-gray-700 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"  type="text" mb-3'
          />
          <h1 className="mb-3 font-medium">Type d évènement : </h1>
          <div className="inline-block relative w-full mb-3">
            <select className="block appearance-none w-full bg-white border border-gray-500 hover:border-gray-700 px-4 py-3 pr-8 rounded focus:outline-none focus:shadow-outline">
              <option>Festival</option>
              <option>Salon & Foire</option>
              <option>Concert & Spectacle</option>
              <option>Tourisme & Parc</option>
              <option>Sport & Session loisirs</option>
              <option>Soirée & Evènement Etudiant</option>
            </select>
            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
              <svg
                className="fill-current h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
              </svg>
            </div>
          </div>

          <div className="ctn_detail mt-2 mb-3 flex items-center ml-1">
            <FaPlus className="cursor-pointer" />
            <h1
              className="ml-1 cursor-pointer"
              onClick={() => setIsShow(!isShow)}
            >
              Ajouter une autre information
              <span className="opacity-50 ml-2">(Optionnel)</span>
            </h1>
          </div>

          {isShow && (
            <div className="ctn_detail_box bg-gray-100 py-3 px-2">
              <div className="ctn_detail_info">
                <label htmlFor="" className="ml-1">
                  Détail
                </label>
                <input
                  type="text"
                  className='appearance-none block w-full text-gray-700 border border-gray-500 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"  type="text" mb-3 mt-2'
                />
              </div>
              <div className="ctn_nv_input w-full h-34">
                <label htmlFor="" className="ml-1 mb-5">
                  Sponsor
                </label>
                <div className="ctn_all_logo flex mb-2 mt-2">
                  {choixImage.map((file, index) => (
                    <>
                      <div key={index}>
                        <img
                          src={URL.createObjectURL(file)}
                          alt=""
                          style={{ maxWidth: "150px", maxHeight: "150px" }}
                          className="w-14 h-14 ml-2"
                          onClick={() => handleRemoveLogo(file.id || index)}
                        />
                      </div>
                    </>
                  ))}
                </div>
                <input
                  type="file"
                  multiple
                  onChange={selectImage}
                  ref={inputRefLogo}
                  style={{ display: "none" }}
                />
                <label
                  htmlFor="uploadBtn"
                  className="label_upload ml-2"
                  onClick={handleClickLogo}
                >
                  Importer une photo (logo)
                </label>
              </div>
            </div>
          )}

          <div className="clt_choix_image ml-2 mt-5">
            <div className=" flex items-center mb-4">
              <h1>Choisiser votre image</h1>
              <img
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAACnklEQVR4nOWXzWsTQRTApxWiiB68iKAH6bEH0UuT1hSPIm4MFHvxKvUgFNGDF8EFM6+beGvxYMCdiQUvSym9eq1Y8V/wIgqJbeZt7MEPROnK252NdZNttjFZhD54MJmZN+83b968zTB24GWczWayzKjkmNHIsYI3IH0VBjbLjNfR8Swz6jlmlMk3o8YAHYe6HgIQTPw8o0yEdfoxyYpTaaVDlhn5MBIspEk7F9t+c/8rgGN6GcGxIgAbkmNdApapLzUACViWgF5Ey+kBcH/Xnii5U3aplfcBONZTB7BLrbyA5nT6ANB5BIKjlRqAY3oZH4IisY8kfGFtnxCg3pJSu2+AfkSa749IjuvtiIF6UzXrR1MBcBzvkAC1GjhXHwP1IVZpbOgAgqulIFHVdg1a52zAcQnKDSCwOlQAwdHUSfqNbk3Yby9gVnD8oo/kYV8AzyrqOJ0lKbWj4xKaczrsP2sL6lonnCoKrn4Fc5pz+wLwPG9EgnJ2XcU10/RGdy1eIMeCqx0JeDNuEyEkgQjAmcQAAtQjbdgi1UnFg0XdixRyXaAexDnvdkxkm6ASurO0M5+au5cDpbbaIYftBOP4pJfzP2viU31c7p4Akm+dD5PHBrzb3kXJvRepjmvdrlic0PEJUCtkGwuwbH46Kbj6oMMtO0IJSoZJJ63PZ5M6jxarrgAOlV9dyQRXG4uL7w5HF6A+GgsrXbc5vYRKdFcAAVjVhaNR43g6dhePt061Kx3HZdaHdABIwHnt/HuN40SvBZ5bzQsS8Ku2ufPPAALUDz/rQd1IuogNeD28KTXuXukLYHK0uEkN69ZGX997stE5g7a1OZbEZoJdnW7/LZ8Zu/9yCA+TpGqx25ecY4Uz8yu5kcIgn2Z76l9PM3bQ5TdeEkOWZvdSbQAAAABJRU5ErkJggg=="
                className="ml-5 cursor-pointer"
                onClick={() => setIsShowChoix(!isShowChoix)}
              ></img>
            </div>

            {isShowChoix && (
              <div className="choix_du_photo w-full flex justify-center bg-gray-100">
                <div className="" onClick={handleImageClick}>
                  {image ? (
                    <div className="ctn_image_choix py-2">
                      <div>
                        <img
                          src={URL.createObjectURL(image)}
                          alt=""
                          className="cursor-pointer image_choix"
                        />
                      </div>
                    </div>
                  ) : (
                    <FaRegImage className="logo_image cursor-pointer" />
                  )}
                  <input
                    type="file"
                    ref={inputref}
                    onChange={handleImageChange}
                    style={{ display: "none" }}
                  />
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="ctn_localisation mb-5 mt-5">
          <div className="ctn_locate shadow-md flex pb-3 mb-4">
            <IoLocationOutline className="iconSquar ml-2 mt-1" />
            <div className="ctn_info_locate">
              <h1 className="font-bold text-arapawa-800 ml-3">Localisation</h1>
              <p className="opacity-50 ml-3">
                Préciser ou se situe votre évènement
              </p>
            </div>
          </div>

          <input
            type="text"
            placeholder="Nom du lieu "
            className='appearance-none block w-full text-gray-700 border border-gray-500 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"  type="text" mb-3'
          />
        </div>

        <div className="ctn_date mb-5">
          <div className="ctn_date shadow-md flex pb-3 mb-4">
            <MdOutlineDateRange className="iconSquar ml-2 mt-1" />
            <div>
              <h1 className="ml-3 font-bold text-arapawa-800">Date</h1>
              <p className="opacity-50 ml-3">
                Préciser ou se situe votre évènement
              </p>
            </div>
          </div>

          <div className="ctn_info_date flex">
            <div className="ctn_date_debut">
              <h1 className="mb-3">Date de début</h1>
              <input type="Date" className="border border-gray-300 py-2 px-5" />
            </div>
            <div className="ctn_heurre_debut ml-5">
              <h1 className="mb-3">Heurre de début</h1>
              <input type="Time" className="border border-gray-300 py-2 px-5" />
            </div>
            <div className="ctn_heurre_de_fin ml-5">
              <h1 className="mb-3">
                Heurre de fin: <span className="opacity-50">(Optionnel)</span>
              </h1>
              <input type="Time" className="border border-gray-300 py-2 px-5" />
            </div>
          </div>
        </div>
        <div className="ctn_tarif mb-5">
          <div className="ctn_date shadow-md flex pb-3 mb-4">
            <BsTicketPerforated className="iconSquar ml-2" />
            <div>
              <h1 className="ml-3 font-bold text-arapawa-800">Tarif</h1>
              <p className="opacity-50 ml-3">
                Préciser ou se situe votre évènement
              </p>
            </div>
          </div>

          <div className="ctn_table flex justify-center items-center mt-9">
            <table className="table-auto text-black border-2">
              <thead>
                <tr>
                  <th className="bgz_type px-4 py-2 text-white">
                    Type de billet
                  </th>
                  <th className="bgz_s    border px-16 py-2 text-white">
                    Simple
                  </th>
                  <th className="bgz_si   border px-16 py-2 text-white">
                    Silver
                  </th>
                  <th className="bgz_g    border px-16 py-2 text-white">
                    Gold
                  </th>
                </tr>
              </thead>

              <tbody>
                <tr>
                  <td className="border px-16 py-2">
                    Nombre de billet disponible
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />
                  </td>
                </tr>
                <tr className="">
                  <td className="border px-16 py-2">Archive</td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                    />{" "}
                  </td>
                </tr>
                <tr>
                  <td className="border px-16 py-2">Total</td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                      disabled
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                      disabled
                    />
                  </td>
                  <td className="border px-8 py-2">
                    <input
                      type="text"
                      className="ctn-input outline-none bg-transparent w-20"
                      disabled
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div className="ctn_button flex justify-center">
          <button className="btn mb-5 text-white font-medium py-2 px-5 rounded">
            Publier mon évènement
          </button>
        </div>
      </div>
    </>
  );
}
