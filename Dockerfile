# Use Python 3.12.8 as the base image
#FROM python:3.12.8-slim
FROM public.ecr.aws/docker/library/python:3.12.8-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy requirements (if exists) or install dependencies inline
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || \
    pip install --no-cache-dir flask flask-swagger-ui

# Copy the application code into the container
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Define the command to run the application
# CMD ["python", "app.py"]
CMD ["flask", "run", "--host=0.0.0.0"]