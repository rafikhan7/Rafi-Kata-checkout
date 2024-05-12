# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /kata-checkout
# Copy the current directory contents into the container at /kata-checkout
COPY . /kata-checkout


# Run the test case file when the container launches
CMD ["python", "runtests.py"]
