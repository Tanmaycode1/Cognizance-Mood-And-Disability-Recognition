# Cognizance Mood and Disability Recognition

## Introduction

The goal of this project is to develop a user-friendly web application that integrates EEG datasets to perform real-time analysis of brain waves. The application aims to assist therapists and clients in monitoring mental health conditions, particularly schizophrenia and epilepsy. By analyzing brain wave patterns, the application provides insights into the presence of these conditions, aiding in early detection and timely intervention.

## Features

1. **Real-time EEG Analysis:** The application processes incoming EEG data in real time, enabling instant feedback on the patient's brain wave patterns.

2. **Schizophrenia Detection:** Utilizing machine learning models trained on relevant datasets, the application can identify potential indicators of schizophrenia in the EEG data.

3. **Epilepsy Detection:** Similar to schizophrenia detection, the application employs machine learning techniques to recognize patterns associated with epilepsy in EEG recordings.

4. **User-Friendly Interface:** The web interface is designed to be intuitive and accessible for both therapists and clients, making it easy to interpret the results.

5. **Secure User Profiles:** Therapists and clients can create accounts with secure profiles, allowing them to track progress over time.

6. **Data Privacy:** The application ensures patient data privacy and complies with relevant regulations (e.g., HIPAA).

## Project Structure

- **.idea:** Configuration files for JetBrains IDE (optional).
- **__pycache__:** Cached Python files (can be ignored).
- **instance:** Configuration files (sensitive information like API keys should be stored here).
- **website:** Frontend code for the web application.
- **emotions.csv:** Dataset file.
- **mail.py:** Python script for handling email functionality.
- **main.py:** Main Flask application script.
- **model_2.keras:** Trained machine learning model file.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Tanmaycode1/Cognizance-Mood-And-Disability-Recognition.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Open the application in your web browser at `http://localhost:5000`.

## Contributors

- [arnavgupta16](https://github.com/arnavgupta16)
- [Tanmaycode1](https://github.com/Tanmaycode1)


