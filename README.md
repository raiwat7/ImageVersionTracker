# Docker Image Metadata Logger

This project is a Python-based application that scans Docker images, extracts their metadata, and logs the information into a JSON file. It also provides a FastAPI-based REST API to retrieve the logged metadata and scan individual images.

## Features

- **Scan Docker Images**: Extract metadata from Docker images and log it.
- **REST API**: 
  - `GET /history`: Retrieve the history of logged metadata.
  - `POST /scan`: Scan a specific Docker image by its tag and log its metadata.
- **Periodic Scanning**: A script to scan all available Docker images and log their metadata.

## Project Structure

- `app/docker_client.py`: Provides a Docker client instance.
- `app/logger.py`: Handles logging and reading metadata from the `image_log.json` file.
- `app/metadata.py`: Extracts metadata from Docker images.
- `app/routes.py`: Defines FastAPI routes for the REST API.
- `main.py`: Entry point for the FastAPI application.
- `periodic_scan.py`: Script to periodically scan all Docker images.
- `image_log.json`: JSON file where metadata is logged (ignored by Git).

## Requirements

- Python 3.8+
- Docker installed and running
- Pip dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
   
2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Ensure Docker is installed and running on your system.

## Usage
### Running the FastAPI Application
1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```
2. Access the API documentation at http://localhost:8000/docs.

### API Endpoints
* GET /history: Retrieve the history of logged metadata.
* POST /scan: Scan a specific Docker image by providing its tag in the request body:
{
  "image_tag": "image_name:tag"
}

### Periodic Scanning
1. Run the `periodic_scan.py` script to scan all Docker images:

    ```bash
    python periodic_scan.py
    ```
2. The metadata will be logged in `image_log.json`.


## Example
1. Scan a specific image using the API:

    ```bash
    curl -X POST "http://localhost:8000/scan" -H "Content-Type: application/json" -d '{"image_tag": "nginx:latest"}'
   ```
2. Retrieve the scan history:

    ```bash
    curl -X GET "http://localhost:8000/history"
   ```
3. Run the periodic scan:

    ```bash
    python periodic_scan.py
   ```
## Notes
* The `image_log.json` file is ignored by Git as specified in `.gitignore`.
* Ensure Docker images are tagged properly to avoid skipping untagged images during scanning.