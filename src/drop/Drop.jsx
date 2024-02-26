import { useRef, useState } from "react";
import "./Drop.css";

export default function Drop() {
  const [images, setImages] = useState([]);
  const [isDragging, setisDragging] = useState(false);
  const fileInputRef = useRef(null);

  function selectFiles() {
    fileInputRef.current.click();
  }

  function onFileSelect(event) {
    const files = event.target.files;
    if (files.length === 0) return;
    for (let i = 0; i < files.length; i++) {
      if (files[i].type.split("/")[0] !== "image") continue;
      if (!images.some((e) => e.name === files[i].name)) {
        setImages((prevImage) => [
          ...prevImage,
          {
            name: files[i].name,
            url: URL.createObjectURL(files[i]),
          },
        ]);
      }
    }
  }

  function deleteImage(index) {
    setImages((prevImage) => {
      prevImage.filter((_, i) => i !== index);
    });
    //console.log(index);
  }

  function onDragOver(event) {
    event.preventDefault();
    setisDragging(true);
    event.dataTransfer.dropEffect = "copy";
  }

  function onDragLeave(event) {
    event.preventDefault();
    setisDragging(false);
  }

  function onDrop(event) {
    event.preventDefault();
    setisDragging(false);
    const files = event.dataTransfer.files;
    for (let i = 0; i < files.length; i++) {
      if (files[i].type.split("/")[0] !== "image") continue;
      if (!images.some((e) => e.name === files[i].name)) {
        setImages((prevImage) => [
          ...prevImage,
          {
            name: files[i].name,
            url: URL.createObjectURL(files[i]),
          },
        ]);
      }
    }
  }

  return (
    <div className="card">
      <div className="top">
        <p>Drag & Drop upload</p>
      </div>

      <div
        className="drag-area"
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
      >
        {isDragging ? (
          <span className="select">Drop images here</span>
        ) : (
          <>
            Drag & Drop images here or{" "}
            <span className="select" role="button" onClick={selectFiles}>
              Browses
            </span>
          </>
        )}

        <input
          name="file"
          type="file"
          className="file"
          multiple
          ref={fileInputRef}
          onChange={onFileSelect}
        />
      </div>

      <div className="container">
        {images.map((images, index) => (
          <div className="image" key={index}>
            <span className="delete" onClick={() => deleteImage(index)}>
              {" "}
              X{" "}
            </span>
            <img src="images.url" alt="images.name" />
          </div>
        ))}
      </div>
      <button type="button">upload</button>
    </div>
  );
}
