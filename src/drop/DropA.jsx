import { useState } from "react";

function FileUpload() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [selectImage, setSelectImage] = useState([]);

  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    setSelectedFiles(files);
  };

  const choixImage = (e) => {
    const files = Array.from(e.target.files);
    setSelectImage(files);
  };

  return (
    <>
      <input type="file" multiple onChange={handleFileChange} />
      <div className="flex justify-between">
        {selectedFiles.map((file, index) => (
          <>
            <div key={index} className="bg-gray-500">
              {file.name}
              <img
                src={URL.createObjectURL(file)}
                alt=""
                style={{ maxWidth: "150px", maxHeight: "150px" }}
              />
            </div>
          </>
        ))}
      </div>
      <div className="separateurUp w-full h-5 bg-red-500"></div>
      <div className="flex justify-between ctn_all_images">
        {selectImage.map((file, index) => (
          <>
            <div key={index}>
              {file.name}
              <img
                src={URL.createObjectURL(file)}
                alt=""
                style={{ maxWidth: "150px", maxHeight: "150px" }}
              />
            </div>
          </>
        ))}
      </div>
      <input type="file" multiple onChange={choixImage} />
    </>
  );
}

export default FileUpload;
