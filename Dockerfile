# Use an appropriate base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the model file and the FastAPI app into the container
COPY artifacts/models/kmeans_model.pkl main.py ./

# Install FastAPI and scikit-learn (or any other dependencies your model requires)
RUN pip install fastapi uvicorn scikit-learn

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



