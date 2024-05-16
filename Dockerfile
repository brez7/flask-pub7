# Set base image (host OS)
FROM python:3.12-alpine


# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
ENTRYPOINT ["python", "app.py"]