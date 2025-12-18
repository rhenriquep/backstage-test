#!/usr/bin/env python3
"""
Simple Python Flask application for Backstage testing.
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Root endpoint that returns a greeting."""
    return jsonify({
        "message": "Hello from Python App!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "python-app"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

