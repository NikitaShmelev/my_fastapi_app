# How to deploy to GCP

```bash
gcloud builds submit --config cloudbuild.yaml
```
```bash
gcloud run deploy fastapi-app \                     
    --image gcr.io/PROJECT_ID/fastapi-app \
    --platform managed \
    --region REGION \
    --allow-unauthenticated
```


```bash
uvicorn app.main:app --reload
```