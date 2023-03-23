FROM python:3.9-slim-buster

# update package list and install dependencies
RUN apt-get update && apt-get install -y \
    libavcodec58 \
    libavformat58 \
    libavutil56 \
    libswresample3 \
    && rm -rf /var/lib/apt/lists/*

# copy the application code to the container
COPY . /app

# set the working directory to the application directory
WORKDIR /app

# install the required Python packages
RUN pip3 install -r requirements.txt

# expose port 80
EXPOSE 80

# start the application
CMD ["python3", "app.py"]