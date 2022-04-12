import React, { useState } from "react";
import axios from "axios";

const UploadForm = () => {
  const [file, setFile] = useState(null);

  const handleFileOnChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleOnSubmit = (e) => {
    e.preventDefault();
    const url = "http://localhost:8001/file_service/upload_file";
    let formData = new FormData();
    formData.append("uploaded_file", file);

    axios
      .post(url, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        responseType: "arraybuffer",
      })
      .then((response) => {
        const tempUrl = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = tempUrl;
        link.setAttribute("Download", "file.csv");
        document.body.appendChild(link);
        link.click();
      });
  };
  return (
    <>
      <form onSubmit={handleOnSubmit}>
        <input onChange={handleFileOnChange} type="file"></input>
        <input type="submit"></input>
      </form>
    </>
  );
};

export default UploadForm;
