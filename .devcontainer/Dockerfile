FROM python:3.9-slim

# Install system dependencies for building hunspell bindings
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libhunspell-dev \
    hunspell \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install build dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel cython

# Set working directory
WORKDIR /workspaces/dutch-pluralizer-py

# Copy entire project
COPY . .

# Install dev dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Install package in development mode
RUN pip install --no-cache-dir -e .