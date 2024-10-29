# Use the official Python slim image
FROM python:3.9-slim

# Install required system packages and LibreOffice
RUN apt-get update && apt-get install -y \
    libreoffice \
    libxrender1 \
    libxext6 \
    libfontconfig1 \
    libfreetype6 \
    libx11-6 \
    libxcb1 \
    libx11-data \
    xfonts-base \
    xfonts-75dpi \
    xfonts-utils \
    xfonts-100dpi \
    xfonts-encodings \
    xfonts-scalable \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /PDF_CONVERTER

# Copy the current directory contents into the container at /PDF_CONVERTER
COPY . /PDF_CONVERTER

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Define environment variable
ENV FLASK_APP app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
