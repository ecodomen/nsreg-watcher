#!/usr/bin/env bash

 sendEmail -f rezvmaria@gmail.com        \
            -t rezvmaria@gmail.com    \
            -s smtp.gmail.com:587  \
            -xu rezvmaria@gmail.com       \
            -xp rxxmtlhpectgckej       \
            -o tls=yes \
            -o message-file=/home/rezvov_vadim/projects/nsreg-watcher/logs/grabber_errors.log \
            -a /home/rezvov_vadim/projects/nsreg-watcher/logs/grabber_errors.log \
            -u "Nsreg grabber failed with errors"

