#!/bin/bash
cd /home/ubuntu/AWS-Continuous-Integration-Project/simple-python-app
python3 -m venv venv || true
source venv/bin/activate
pip install -r requirements.txt
