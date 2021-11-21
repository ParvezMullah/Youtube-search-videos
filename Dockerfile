FROM ubuntu:18.04
FROM python:3.7.3
ENV PYTHONUNBUFFERED=1
COPY requirements.text /fampay/
RUN pip install -r /fampay/requirements.text
COPY . /fampay/

#cron
RUN apt-get update && apt-get -y install cron

# Copy fetch-video-cron file to the cron.d directory
COPY youtube_search_videos/search_videos/fetch-video-cron /etc/cron.d/fetch-video-cron

# Give execution rights on the cron job
RUN chmod 0600 /etc/cron.d/fetch-video-cron

# Apply cron job
RUN crontab /etc/cron.d/fetch-video-cron

# Create the log file to be able to run tail
RUN touch /var/log/fetch-video-cron.log

CMD /usr/sbin/cron -f

WORKDIR /fampay