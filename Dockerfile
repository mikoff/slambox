# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Set the working directory
WORKDIR /workspace

# Install OS packages 
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget nano gcc g++ apt-transport-https ca-certificates x11-apps lsb-release sudo

# Install development packages
RUN apt-get install -y build-essential cmake pkg-config software-properties-common \
    git libboost-all-dev libgtest-dev clang libva-dev libtbb-dev \
    python3-dev python3-pip python3-venv

# Optional: Configure user and permissions for devcontainers
# Create a non-root user
RUN useradd -m -s /bin/bash vscode && \
    chown -R vscode:vscode /home/vscode

### setup python environment
USER vscode
# Create virtual environment for python
ENV PYTHON_VENV=/home/vscode/venv/slambox
RUN python3 -m venv $PYTHON_VENV
ENV PATH="$PYTHON_VENV/bin:$PATH"
COPY requirements.txt .
RUN pip3 install -r requirements.txt

USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*