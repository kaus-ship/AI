import { useState } from "react";

import {
  uploadPDF,
  uploadPPT,
  addWebsite,
  addYoutube
} from "../services/api";

function UploadPanel() {

  const [status, setStatus] =
    useState("");

  const [websiteUrl,
    setWebsiteUrl] =
    useState("");

  const [youtubeUrl,
    setYoutubeUrl] =
    useState("");

  const handlePDF =
    async (e) => {

      const file =
        e.target.files[0];

      if (!file) return;

      try {

        await uploadPDF(file);

        setStatus(
          "PDF uploaded successfully"
        );

      } catch {

        setStatus(
          "PDF upload failed"
        );

      }
    };

  const handlePPT =
    async (e) => {

      const file =
        e.target.files[0];

      if (!file) return;

      try {

        await uploadPPT(file);

        setStatus(
          "PPT uploaded successfully"
        );

      } catch {

        setStatus(
          "PPT upload failed"
        );

      }
    };

  const handleWebsite =
    async () => {

      try {

        await addWebsite(
          websiteUrl
        );

        setStatus(
          "Website added successfully"
        );

        setWebsiteUrl("");

      } catch {

        setStatus(
          "Website add failed"
        );

      }
    };

  const handleYoutube =
    async () => {

      try {

        await addYoutube(
          youtubeUrl
        );

        setStatus(
          "YouTube added successfully"
        );

        setYoutubeUrl("");

      } catch {

        setStatus(
          "YouTube add failed"
        );

      }
    };

  return (

    <div>

      <h2>
        Upload Sources
      </h2>

      <div>

        <h3>PDF</h3>

        <input
          type="file"
          accept=".pdf"
          onChange={handlePDF}
        />

      </div>

      <div>

        <h3>PPT</h3>

        <input
          type="file"
          accept=".ppt,.pptx"
          onChange={handlePPT}
        />

      </div>

      <div>

        <h3>
          Website URL
        </h3>

        <input
          type="text"
          value={websiteUrl}
          onChange={(e) =>
            setWebsiteUrl(
              e.target.value
            )
          }
          placeholder="Enter website URL"
        />

        <button
          onClick={handleWebsite}
        >
          Add Website
        </button>

      </div>

      <div>

        <h3>
          YouTube URL
        </h3>

        <input
          type="text"
          value={youtubeUrl}
          onChange={(e) =>
            setYoutubeUrl(
              e.target.value
            )
          }
          placeholder="Enter YouTube URL"
        />

        <button
          onClick={handleYoutube}
        >
          Add Video
        </button>

      </div>

      <p>{status}</p>

    </div>
  );
}

export default UploadPanel;