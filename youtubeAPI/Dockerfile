FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /youtubeAPI

# Set the working directory to /youtube_data_feed
WORKDIR /youtubeAPI

# Copy the current directory contents into the container at /youtube_data_feed
ADD . /youtubeAPI/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
