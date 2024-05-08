 # Use an official Python runtime as a parent image
# FROM python:3

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Expose port 80 to allow external access
# EXPOSE 80

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["python", "app.py"]

# Use an official Python runtime as a parent image
FROM python:3

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 80 to allow external access (if needed)
EXPOSE 80

# Start the tkinter application
CMD ["python", "app.py"]
