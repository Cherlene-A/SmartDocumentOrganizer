# SmartDocumentOrganizer

A Python-based document organizer that automatically categorizes files (e.g., docs, junk, important) into folders using keyword matching.

---

## 🔍 Overview

SmartDocumentOrganizer helps you clean up and manage messy document folders by automatically sorting files based on predefined keywords. It groups documents into organized folders so you can find what you need faster.

---

## 🚀 Features

- 📁 Automatically sorts files into categories like **important**, **junk**, and **categorized**  
- 🔑 Keyword-based classification (customizable via text files)  
- 🧠 Simple automation for local document management  
- 🐍 Built with Python

---

## 📦 Project Structure

SmartDocumentOrganizer/

├── categorized/

├── documents/

├── static/

├── templates/

├── important_keywords.txt

├── junk_keywords.txt

├── main.py

├── requirements.txt


---

## 🛠️ Tech Stack

- **Language:** Python  
- **Other:** Text-based keyword lists for classification  
- **Dependencies:** See `requirements.txt` 

---

## 📥 Installation

1. Clone this repository:
git clone https://github.com/Cherlene-A/SmartDocumentOrganizer.git

Change directory:

cd SmartDocumentOrganizer


Install Python dependencies:

pip install -r requirements.txt

▶️ Usage

Add your documents into the documents/ folder.

Update important_keywords.txt and junk_keywords.txt with terms you care about.

Run the organizer:

python main.py


Check the categorized/ folder to find sorted documents.

⚙️ How It Works

This tool reads all files in the documents folder, looks for keyword matches based on your text files, and moves each file to a classification folder.
You can customize the keywords to fit your personal filing needs.

## 🚀 Live Demo  
Experience the Smart Document Organizer live here:  
👉  https://smartdocumentorganizer.onrender.com/









