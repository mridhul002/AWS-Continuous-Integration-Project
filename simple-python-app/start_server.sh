#!/bin/bash
cd /home/ubuntu/AWS-Continuous-Integration-Project/simple-python-app
source venv/bin/activate
nohup python app.py > app.log 2>&1 &
