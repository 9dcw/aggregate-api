FROM python:3.9
# Use the python latest image
COPY . ./

# Copy the current folder content into the docker image
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Install the required packages of the application
CMD gunicorn --bind :$PORT app:app
# Bind the port and refer to the app.py app