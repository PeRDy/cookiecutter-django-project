FROM python:{{ cookiecutter.python_version }}-slim

RUN apt-get update && \
    apt-get install -y \
        locales \
        locales-all
ENV LANG='es_ES.UTF-8' LANGUAGE='es_ES.UTF-8:es' LC_ALL='es_ES.UTF-8'

# Install build requirements
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        apt-transport-https \
        git \
        curl

# Install Node
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get install -y \
        nodejs

# Add Phusion ppa
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
RUN echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie main > /etc/apt/sources.list.d/passenger.list

# Install system requirements
RUN apt-get update && \
    apt-get install -y \
        libpq-dev \
        passenger

# Create project dirs
RUN mkdir -p /srv/apps/{{ cookiecutter.project_slug }}/logs
WORKDIR /srv/apps/{{ cookiecutter.project_slug }}

# Install pip requirements
COPY requirements.txt constraints.txt /srv/apps/{{ cookiecutter.project_slug }}/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -c constraints.txt

# Install Gulp and Bower
RUN npm install -g gulp bower

# Clean up
RUN apt-get clean && \
    apt-get purge --auto-remove -y \
        build-essential \
        apt-transport-https && \
    rm -rf $HOME/.cache/pip/* \
        /tmp/* \
        /etc/apt/sources.list.d/passenger.list \
        /var/tmp/* \
        /var/lib/apt/lists/* \
        /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin

# Copy application
COPY . /srv/apps/{{ cookiecutter.project_slug }}/

RUN npm install && gulp bower && gulp default:dist

ENTRYPOINT ["./run.py"]
