# Vchile Number Plate Detection System

## 📌 Project Description

This project is a Computer Vision and embedded system – based number plate detection that performs:

- Real-time vehicle detection  
- Automatic number plate recognition  
- Streaming video input from ESP32-CAM  
- Optical Character Recognition using Tesseract OCR  
- Data storage in MySQL Database with timestamp  

The system is designed to replace physical IoT sensors with a laptop camera and ESP32-CAM stream, providing a low-cost and intelligent parking entry management solution.

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- Tesseract OCR  
- MySQL Database  
- ESP32-CAM Module  

---

## 🚀 Features

- Detects number plates from live ESP32-CAM video stream  
- Extracts plate text using OCR  
- Displays detected plate on screen  
- Automatically stores:
  - Plate number  
  - Entry time  

- Works continuously with real-time processing

---

## 📂 Project Structure

smart-parking-plate-detection/
│
├── main.py
├── config.py
├── requirements.txt
├── best.pt
└── screenshots/

---

## ⚙️ Setup Instructions

### Step 1 – Install Requirements

Run the following command:

pip install -r requirements.txt

---

### Step 2 – Configure Tesseract OCR

Install Tesseract OCR and update its path in `config.py`:

Example path:

C:/Program Files/Tesseract-OCR/tesseract.exe

---

### Step 3 – MySQL Database Setup

Create a MySQL database named:

parking_db

And a table:

car_entries

Columns:

- plate_number  
- entry_time  

---

### Step 4 – Run the Application

python main.py

Make sure ESP32-CAM is streaming and accessible via local network.

---

## 📷 Output

The application window shows:

- Live video  
- Detected plate bounding box  
- Recognized plate text  

Database log prints stored plate details in terminal.

---

## 🔒 Security Note

- Do NOT upload real credentials  
- Use `.gitignore` for config files  
- Replace passwords with placeholder text before pushing to GitHub

---

## 🎯 Future Enhancements

- Parking slot occupancy detection  
- Voice-based parking guidance  
- Automated billing system  
- Entry and exit management  
- Web dashboard integration

---

## 👤 Author

Developed by:  
**Sahaya Parthi R**  
ECE – Final Year Student  
Anna University Regional Campus, Tirunelveli

---

## 📄 License

This project is open-source and free to use for educational purposes.
