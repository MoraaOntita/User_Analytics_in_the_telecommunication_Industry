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

# Command to run the Flask app
CMD ["python", "app.py"]

