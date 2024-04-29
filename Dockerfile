FROM python:3.8-slim
WORKDIR /app
COPY artifacts/models/kmeans_model.pkl .


