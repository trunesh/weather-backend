# 🌤️ Weather Data Backend API (GCP + Flask)

Hi there! This is a small backend service I built for InRisk Labs' backend developer challenge. It fetches historical weather data using the Open-Meteo API and stores the response in JSON format on Google Cloud Storage (GCS). The app is built with Flask, Dockerized, and deployed on Google Cloud Run.

Live URL: **https://weather-backend-4xthn453fq-el.a.run.app**

---

## 🛠️ Tech Stack
- **Python 3.10** + Flask
- **Google Cloud Run** (Containerized)
- **Google Cloud Storage (GCS)**
- **Docker**
- **Open-Meteo Historical Weather API**

---

## 🚀 API Endpoints

1. /store-weather-data POST
Request:
(venv) trunu:~/Desktop/pyProjects/weather-backend$ curl -X POST https://weather-backend-4xthn453fq-el.a.run.app/store-weather-data -H "Content-Type: application/json" -d '{
  "latitude": 19.07,
  "longitude": 72.87,
  "start_date": "2025-05-01",
  "end_date": "2025-05-05"
}'
{
  "file_name": "weather_19.07_72.87_2025-05-01_to_2025-05-05.json",
  "message": "Weather data stored successfully"
}


2. GET /list-weather-files

(venv) trunu:~/Desktop/pyProjects/weather-backend$ curl https://weather-backend-4xthn453fq-el.a.run.app/list-weather-files
{
  "files": [
    "weather_19.07_72.87_2024-05-01_to_2024-05-05.json",
    "weather_19.07_72.87_2025-05-01_to_2025-05-05.json"
  ]
}

3. GET /weather-file-content/<file_name>
https://weather-backend-4xthn453fq-el.a.run.app/weather-file-content/weather_19.07_72.87_2024-05-01_to_2024-05-05.json

{
  "daily": {
    "apparent_temperature_max": [
      37.0,
      37.8,
      38.7,
      39.1,
      41.0
    ],
    "apparent_temperature_mean": [
      33.0,
      32.9,
      32.8,
      34.2,
      34.9
    ],
    "apparent_temperature_min": [
      29.3,
      29.2,
      27.8,
      29.4,
      30.7
    ],
    "temperature_2m_max": [
      34.6,
      33.5,
      33.3,
      33.3,
      34.8
    ],
    "temperature_2m_mean": [
      29.6,
      28.8,
      28.2,
      28.9,
      30.0
    ],
    "temperature_2m_min": [
      25.2,
      24.4,
      23.4,
      24.2,
      25.0
    ],
    "time": [
      "2024-05-01",
      "2024-05-02",
      "2024-05-03",
      "2024-05-04",
      "2024-05-05"
    ]
  },
  "daily_units": {
    "apparent_temperature_max": "\u00b0C",
    "apparent_temperature_mean": "\u00b0C",
    "apparent_temperature_min": "\u00b0C",
    "temperature_2m_max": "\u00b0C",
    "temperature_2m_mean": "\u00b0C",
    "temperature_2m_min": "\u00b0C",
    "time": "iso8601"
  },
  "elevation": 6.0,
  "generationtime_ms": 0.20945072174072266,
  "latitude": 19.086115,
  "longitude": 72.85291,
  "timezone": "Asia/Kolkata",
  "timezone_abbreviation": "GMT+5:30",
  "utc_offset_seconds": 19800
}




## 📦 How to Run Locally

### 1. Clone the repo & install dependencies
```bash
git clone https://github.com/your-username/weather-backend.git
cd weather-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set environment variables
```bash
export GCS_BUCKET_NAME=your-bucket-name
export GOOGLE_APPLICATION_CREDENTIALS="/full/path/to/key.json"
```

### 3. Start the Flask app
```bash
cd app
python main.py
```

---

## 🐳 Docker Build & GCP Deploy

### Build the image:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/weather-backend
```

### Deploy to Cloud Run:
```bash
gcloud run deploy weather-backend   --image gcr.io/YOUR_PROJECT_ID/weather-backend   --platform managed   --region asia-south1   --allow-unauthenticated   --set-env-vars GCS_BUCKET_NAME=your-bucket-name
```

---

##  Notes
- Container listens on port `8080` as required by Cloud Run
- GCS bucket needs `objectAdmin` permission for the service account
- Initially ran into the **GCP billing not enabled** error — nothing like getting blocked before writing a single line of backend logic
- Flask wasn’t listening on the right port (`8080` instead of `5000`) for Cloud Run — fixed that after some nice debugging

Thank you
