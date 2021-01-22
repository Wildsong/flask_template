FROM continuumio/miniconda3
LABEL maintainer="Brian Wilson <brian@wildsong.biz>"
LABEL version="1.0"
LABEL biz.wildsong.name="flask-template"

ENV SERVER_BASE /srv

# This will upgrade conda, so the fact that the base image is old does not matter
#
RUN conda update -n base -c defaults conda

# Add some sources to conda, so we can load more packages if we want.
RUN conda config --add channels conda-forge &&\
    conda config --add channels hugo &&\
    conda config --add channels Esri


# Install the packages that this project needs.
COPY requirements.txt ./
RUN conda install --file requirements.txt

# Don't run as root
RUN adduser --disabled-password --gecos '' app

WORKDIR $SERVER_BASE
