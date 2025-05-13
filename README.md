# 🎥 Simple Video Downloader App

A lightweight and easy-to-use web-based video downloader built using **HTML (Frontend)** and **Python (Backend - Flask)**. This app allows users to paste a video URL and download the video directly to their device.

---

## 🚀 Features

- Minimal user interface using HTML and Bootstrap
- Backend built using Python and Flask
- Downloads videos from popular platforms (like Instagram, YouTube(not developed yet) 
- Lightweight and easy to run locally
- Fully open-source

---

## ![Home Page](screenshots/home.png)
> *Simple UI for pasting and downloading videos*

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask

---

## 📦 Installation & Cloning Instructions

Follow these steps to run the app locally:

### 1. Clone the Repository

     ```bash
      git clone https://github.com/your-username/simple-video-downloader.git  
      cd simple-video-downloader

   2.Set Up Virtual Environment (Optional but Recommended)
   
      ```bash
        python -m venv venv 
        source venv/bin/activate   # For Windows: venv\Scripts\activate
  3. Install Dependencies

    ```bash
      pip install -r requirements.txt
     Make sure you have Python 3.7+ installed.

  5. Run the App

    ```bash
      python app.py
     The app will run on:
🌐 http://127.0.0.1:5000

 📁 Project Structure
 
     csharp

    simple-video-downloader/
    ├── templates/
    │
    │   └── index.html           # Frontend HTML
    │
    ├── static/                  # CSS, JS, assets
    │
    ├── app.py                   # Main Flask application
    ├── requirements.txt         # Python dependencies
    └── README.md
 📌 Dependencies
      txt
      Flask
      pytube
You can install them with:

   ```bash
   pip install Flask pytube



