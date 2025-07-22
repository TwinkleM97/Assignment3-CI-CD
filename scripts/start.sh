#!/bin/bash
echo "Installing dependencies..."
pip install -r app/requirements.txt
echo "Starting Random Fun Fact API..."
python3 app/app.py
