FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget nano gcc g++ apt-transport-https ca-certificates x11-apps lsb-release sudo \
    build-essential cmake pkg-config software-properties-common \
    git libboost-all-dev libgtest-dev clang libva-dev libtbb-dev \
    python3-dev python3-pip python3-venv \
    libfontenc-dev libice-dev libsm-dev libva-dev libvdpau-dev libx11-dev libx11-xcb-dev \
    libxau-dev libxaw7-dev libxcb-composite0-dev libxcb-cursor-dev libxcb-dri2-0-dev \
    libxcb-dri3-dev libxcb-ewmh-dev libxcb-glx0-dev libxcb-icccm4-dev libxcb-image0-dev \
    libxcb-keysyms1-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-render-util0-dev \
    libxcb-res0-dev libxcb-shape0-dev libxcb-sync-dev libxcb-util-dev libxcb-xfixes0-dev \
    libxcb-xinerama0-dev libxcb-xkb-dev libxcomposite-dev libxcursor-dev libxdamage-dev \
    libxdmcp-dev libxext-dev libxfixes-dev libxi-dev libxinerama-dev libxkbfile-dev \
    libxmu-dev libxmuu-dev libxpm-dev libxrandr-dev libxrender-dev libxres-dev libxss-dev \
    libxt-dev libxtst-dev libxv-dev libxxf86vm-dev uuid-dev xkb-data \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 1000 developer && \
    useradd -u 1000 -g 1000 -m -s /bin/bash developer && \
    chown -R developer:developer /home/developer

USER developer
WORKDIR /home/developer
ENV PYTHON_VENV=/home/developer/venv/development
RUN python3 -m venv $PYTHON_VENV
ENV PATH="$PYTHON_VENV/bin:$PATH"
COPY requirements.txt .
RUN pip3 install -r requirements.txt
