#!/bin/bash

screen -dmS "chatbot" python ./main.py
screen -dmS "speech" python ./say.py
screen -dmS "listen" python ./listen.py
#screen -dmS "eyes" ~/Desktop/pi-facerec-box-master/start.sh

