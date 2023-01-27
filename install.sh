#!/bin/env bash
python3 -m venv env
source env/bin/activate
pip3 install pip -U
pip3 install -r requirements.txt
