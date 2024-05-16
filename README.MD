 


Browser Sync:
browser-sync start --proxy "http://127.0.0.1:5000" --files "static/*, templates/**/*.html"

Build Docker Image and Deploy to Cloud Run:

Login to gcloud:
gcloud auth login

Set the project: 
gcloud config set project upbeat-button-265722

Build the Docker image: 
docker build -t gcr.io/upbeat-button-265722/rjb .

Test run the app: 
docker run -p 5000:5000 -e PORT=5000 gcr.io/upbeat-button-265722/rjb:latest

Push the Docker image to Cloud Run: 
docker push gcr.io/upbeat-button-265722/rjb

Deploy the image to Cloud Run
gcloud run deploy rjb --image gcr.io/upbeat-button-265722/rjb --platform managed --region us-central1 --allow-unauthenticated

Live Site: 
https://rjb-fvmy7faymq-uc.a.run.app/

LEFTOVERS:
docker build -t rjb .
gcloud auth configure-docker



docker build -t gcr.io/upbeat-button-265722/rjb .; 