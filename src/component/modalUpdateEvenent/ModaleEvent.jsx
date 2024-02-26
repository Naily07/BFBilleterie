import React, { useRef, useState } from "react";
import { FaRegPenToSquare } from "react-icons/fa6";
import { GoSponsorTiers } from "react-icons/go";
import { IoLocationOutline } from "react-icons/io5";
import { MdOutlineDateRange } from "react-icons/md";
import { BsTicketPerforated } from "react-icons/bs";
import "./ModaleEvent.css";

export default function Modal() {
  const [showModal, setShowModal] = React.useState(false);

  const [choixImage, setChoixImage] = useState([]);
  const inputRefLogo = useRef(null);

  const selectImage = (event) => {
    const files = Array.from(event.target.files);
    setChoixImage(files);
  };

  const handleClickLogo = () => {
    inputRefLogo.current.click();
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
      <div className="ctn_icone_update flex mb-1 mr-1">
        <button
          className="flex items-center bg-arapawa-800 text-white text-xs uppercase text-sm px-3 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none ease-linear transition-all duration-150"
          type="button"
          onClick={() => setShowModal(true)}
        >
          <span className="mr-1">
            <FaRegPenToSquare />
          </span>
          Modifier un élément
        </button>
      </div>
      {showModal ? (
        <>
          <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
            <div className="relative w-auto my-6 mx-auto max-w-3xl">
              {/*content*/}
              <div className="ctn_modale_single_page px-3 border-0 rounded-lg shadow-lg relative flex flex-col bg-white outline-none focus:outline-none">
                {/*header*/}
                <div className="flex items-start justify-between p-5 border-b border-solid border-blueGray-200 rounded-t">
                  <h3 className="text-2xl font-semibold">
                    Modifier votre élément
                  </h3>
                  <button
                    className="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
                    onClick={() => setShowModal(false)}
                  >
                    <span className="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                      ×
                    </span>
                  </button>
                </div>
                {/*body*/}
                <div className="ctn_name_event mt-2 mb-2">
                  <div className="flex">
                    <FaRegPenToSquare className="mt-1 text-arapawa-800" />
                    <h1 className="mb-1 text-arapawa-800 font-bold">
                      -Nom de l évènement *
                    </h1>
                  </div>
                  <input
                    type="text"
                    className='appearance-none block w-full text-gray-900 border border-gray-500 hover:border-gray-700 rounded py-2 px-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"  type="text" mb-2'
                  />
                </div>

                <div className="ctn_date_event mb-2">
                  <div className="ctn_info_date flex">
                    <div className="ctn_date_debut">
                      <div className="flex">
                        <MdOutlineDateRange className="mt-1 text-arapawa-800" />
                        <h1 className="mb-1 text-arapawa-800 font-bold">
                          -Date de début
                        </h1>
                      </div>
                      <input
                        type="Date"
                        className="border border-gray-500 py-2 px-5"
                      />
                    </div>
                    <div className="ctn_heurre_debut ml-5">
                      <h1 className="mb-1 text-arapawa-800 font-bold">
                        -Heurre de début
                      </h1>
                      <input
                        type="Time"
                        className="border border-gray-500 py-2 px-5"
                      />
                    </div>
                    <div className="ctn_heurre_de_fin ml-5">
                      <h1 className="mb-1 text-arapawa-800 font-bold">
                        -Heurre de fin:{" "}
                        <span className="opacity-50">(Optionnel)</span>
                      </h1>
                      <input
                        type="Time"
                        className="border border-gray-500 py-2 px-5"
                      />
                    </div>
                  </div>
                </div>

                <div className="ctn_local_event mt-1 mb-2   ">
                  <div className="flex items-center">
                    <IoLocationOutline className="text-arapawa-800" />
                    <h1 className="mb-2 mt-2 text-arapawa-800 font-bold">
                      -Lieu de l évènement
                    </h1>
                  </div>
                  <input
                    type="text"
                    className='appearance-none block w-full text-gray-900 border border-gray-500 rounded py-2 px-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" type="text" mb-3'
                  />
                </div>

                <div className="mb-2">
                  <div className="flex">
                    <GoSponsorTiers className="mt-1  text-arapawa-800 w-4 h-4" />
                    <label htmlFor="" className="text-arapawa-800 font-bold">
                      -Sponsore
                    </label>
                  </div>

                  <div className="ctn_sponsore_modale">
                    <div className="ctn_nv_input w-full h-34">
                      <div className="ctn_all_logo flex mb-2 mt-2">
                        <div className="ctn_imange_logo_modale flex">
                          {choixImage.map((file, index) => (
                            <>
                              <div key={index}>
                                <img
                                  src={URL.createObjectURL(file)}
                                  alt=""
                                  style={{
                                    maxWidth: "150px",
                                    maxHeight: "150px",
                                  }}
                                  className="w-14 h-14 ml-2"
                                  onClick={() =>
                                    handleRemoveLogo(file.id || index)
                                  }
                                />
                              </div>
                            </>
                          ))}
                        </div>
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
                        className="bg-gray-700 text-white px-3 py-1 rounded hover:bg-gray-600 cursor-pointer"
                        onClick={handleClickLogo}
                      >
                        Importer une photo (logo)
                      </label>
                    </div>
                  </div>
                </div>

                <div className="ctn_tarif_single mt-3 mb-4">
                  <div className="flex items-center">
                    <BsTicketPerforated className="text-arapawa-800 ml-1" />
                    <h1 className="text-arapawa-800 font-bold">-Tarif</h1>
                  </div>
                  <div className="ctn_tb_tarif mt-2 flex justify-center">
                    <table>
                      <thead>
                        <tr>
                          <th className="px-4 py-2 bg-arapawa-800 text-white">
                            Type de billet
                          </th>
                          <th className="border bg-arapawa-800 px-5 py-2 text-white">
                            Simple
                          </th>
                          <th className="border bg-arapawa-800 px-5 py-2 text-white">
                            Silver
                          </th>
                          <th className="border bg-arapawa-800 px-5 py-2 text-white">
                            Gold
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td className="border px-16 py-2">Prix</td>
                          <td className="border px-6 py-2">
                            <input
                              type="text"
                              className="ctn-input outline-none bg-transparent w-20"
                            />
                          </td>
                          <td className="border px-6 py-2">
                            <input
                              type="text"
                              className="ctn-input outline-none bg-transparent w-20"
                            />
                          </td>
                          <td className="border px-6 py-2">
                            <input
                              type="text"
                              className="ctn-input outline-none bg-transparent w-20"
                            />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
                {/*footer*/}
                <div className="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
                  <button
                    className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150 border border-red-300 py-3 rounded"
                    type="button"
                    onClick={() => setShowModal(false)}
                  >
                    Annuler
                  </button>
                  <button
                    className="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
                    onClick={() => setShowModal(false)}
                  >
                    Confirmer
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
        </>
      ) : null}
    </>
  );
}
