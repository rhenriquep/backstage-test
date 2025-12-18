# Python App

A simple Python Flask application for testing Backstage integration.

## Description

This is a minimal Python application created to test the Backstage internal developer portal and CI/CD integration.

## Features

- Simple Flask REST API
- Health check endpoint
- CI/CD pipeline with GitHub Actions

## Endpoints

- `GET /` - Returns a greeting message
- `GET /health` - Health check endpoint

## Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application:
- Main endpoint: http://localhost:5000/
- Health check: http://localhost:5000/health

## CI/CD

This project includes a GitHub Actions workflow that:
- Runs on push and pull requests
- Tests the application
- Performs basic linting
- Verifies the app can start

## Owner

rhenrique@ccmtecnologia.com.br

