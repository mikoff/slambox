# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Install OS packages 
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget nano gcc g++ apt-transport-https ca-certificates x11-apps lsb-release sudo

# Install development packages
RUN apt-get install -y build-essential cmake pkg-config software-properties-common git libboost-all-dev libgtest-dev clang libva-dev
RUN apt-get install -y libvdpau-dev xkb-data

### setup python environment
# Install Python 3 packages
RUN apt-get install -y python3-dev python3-pip python3-venv

# Create vscode user
RUN useradd -ms /bin/bash vscode
USER vscode

# Create virtual environment for python
ENV PYTHON_VENV=/home/vscode/venv/slambox
RUN python3 -m venv $PYTHON_VENV
ENV PATH="$PYTHON_VENV/bin:$PATH"
COPY requirements.txt .
RUN pip3 install -r requirements.txt

### setup c++ environment
RUN pip3 install conan

# switch back to root
USER root

# clean everything
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*