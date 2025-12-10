# Dockerfile for VS Code Dev Container
#FROM nrel/openstudio:3.10.0
FROM nrel/energyplus:25.1.0

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Set python3 as default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Install common Python tools
RUN pip3 install --upgrade pip

# Install UV package manager
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN pip3 install uv

# Set working directory
WORKDIR /workspace
