import fs from "fs";
import axios from "axios";
import path from "path";
import { fileURLToPath } from "url";
import NodeWebcam from "node-webcam";


const CONTAINER_URL = process.env.CONTAINER_URL;
const API_KEY = process.env.API_KEY;


// === Configure webcam options ===
const options = {
  width: 640,
  height: 480,
  quality: 90,
  output: "jpeg",
  device: false,
  callbackReturn: "location",
  verbose: false,
};

// Create a webcam instance
const Webcam = NodeWebcam.create(options);
const photoPath = "snapshot.jpg";

// === Capture image from webcam ===
console.log("📸 Capturing image from webcam...");
Webcam.capture(photoPath, async (err) => {
  if (err) {
    console.error("❌ Error capturing webcam image:", err);
    return;
  }

  console.log("✅ Image captured:", photoPath);

  // Encode image in base64
  const imgBase64 = fs.readFileSync(photoPath, { encoding: "base64" });

  const headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json",
  };

  const data = {
    url: "data:image/jpeg;base64," + imgBase64,
    features: ["objects"],
  };

  console.log("🚀 Sending image to Vision container...");

  try {
    const res = await axios.post(CONTAINER_URL, data, { headers });
    console.log("✅ Response status:", res.status);
    console.log(JSON.stringify(res.data, null, 2));
  } catch (err) {
    console.error("❌ Request failed:", err.message);
    if (err.response) {
      console.error("Response:", err.response.status, err.response.data);
    }
  }
});
