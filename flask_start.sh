#!/bin/bash 

. ./venv/bin/activate 
export FLASK_APP=MainScores.py 
flask run --host=0.0.0.0
