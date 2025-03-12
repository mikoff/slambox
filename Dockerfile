# Stage 1: Builder
FROM ubuntu:22.04 AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget nano gcc g++ apt-transport-https ca-certificates x11-apps lsb-release sudo \
    build-essential cmake pkg-config software-properties-common \
    git libboost-all-dev libgtest-dev clang libva-dev libtbb-dev \
    python3-dev python3-pip python3-venv \
    libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user and set working directory
RUN groupadd -g 1000 developer && \
    useradd -u 1000 -g 1000 -m -s /bin/bash developer
USER developer
WORKDIR /home/developer

# Set up virtualenv and upgrade pip
ENV PYTHON_VENV=/home/developer/venv/development
RUN python3 -m venv $PYTHON_VENV && \
    . $PYTHON_VENV/bin/activate && pip install --upgrade pip

# Install Python requirements
COPY --chown=developer:developer requirements.txt .
RUN . $PYTHON_VENV/bin/activate && pip install -r requirements.txt

# Clone symforce into a persistent location and install it in editable mode
RUN . $PYTHON_VENV/bin/activate && \
    git clone --depth 1 https://github.com/symforce-org/symforce.git /home/developer/symforce && \
    ls -la /home/developer/ && \
    cd /home/developer/symforce && pip install -e .

RUN ls -la /home/developer/

# Stage 2: Final runtime image
FROM ubuntu:22.04

# Install minimal runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user for runtime
RUN groupadd -g 1000 developer && \
    useradd -u 1000 -g 1000 -m -s /bin/bash developer
USER developer
WORKDIR /home/developer

# Copy the virtualenv and the symforce source (preserving the path)
COPY --chown=developer:developer --from=builder /home/developer/venv/development /home/developer/venv/development
COPY --chown=developer:developer --from=builder /home/developer/symforce /home/developer/symforce

RUN ls -la /home/developer/

# Update PATH to use the virtualenv
ENV PATH="/home/developer/venv/development/bin:$PATH"
