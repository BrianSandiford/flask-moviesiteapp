#!/bin/bash

echo '### create python 3 virtual enviroment ###'

VIRTUAL_ENV_NAME='virtual-enviroment'
python3 -m venv $VIRTUAL_ENV_NAME

echo '#### Activate virtual enviroment ###"
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install requirements ###'
pip3 install -r ./requirements.txt

### Jump to the Path ####
cd /var/lib/jenkins/workspace/$JOB_NAME/

echo '##### Run Test #####'
# pip3 install Flask
python3 manage.py test

echo '#### deactivate virtual environment ###'
#deactivate 
exit