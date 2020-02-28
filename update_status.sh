#!/bin/bash
function gitpull { /usr/local/bin/git pull || (gitpull) }; #git pull until success
function gitpush { /usr/local/bin/git push || (gitpush) }; #git push until success
#My crontab to run this script every hour looks like:
# 0 * * * * ~/Codes/BPHC-DChubs/update_status.sh >> ~/Codes/BPHC-DChubs/update_status.log 2>&1
/sbin/ping 172.16.0.30 -c 1 -W 1
if [ $? = 0 ]
then
    eval `ssh-agent -s` && ssh-add ~/.ssh/id_ed25519 && cd ~/Codes/BPHC-DChubs && gitpull && /usr/local/bin/python3 dc_status.py && /usr/local/bin/git commit -am "Updated Active Hubs" && gitpush && kill $SSH_AGENT_PID
fi