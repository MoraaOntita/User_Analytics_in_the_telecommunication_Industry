# Use an appropriate base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the model file and the Flask app into the container
COPY artifacts/models/kmeans_model.pkl app.py ./

# Install Flask and scikit-learn (or any other dependencies your model requires)
RUN pip install flask scikit-learn

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]


