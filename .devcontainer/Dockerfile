FROM python:3.13-slim

# Install system dependency: libhunspell
RUN apt-get update && apt-get install -y --no-install-recommends \
    libhunspell-dev \
    hunspell \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Set working directory
WORKDIR /workspaces/dutch-pluralizer-py

# Copy entire project
COPY . .

# Install dev dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Install package in development mode
RUN pip install --no-cache-dir -e .
