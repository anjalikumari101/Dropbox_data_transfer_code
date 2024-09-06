#!/bin/sh
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
PATH="/home/dpc-narmada/.local/bin:/opt/spinnaker/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

export PATH=$PATH
export PYTHONPATH=$PYTHONPATH

cd /home/dpc-narmada/INSIGHTZZ/DROPBOX
nohup python3 /home/dpc-narmada/Insightzz/DROPBOX/dropbox_data_transfer.py > /home/dpc-narmada/Insightzz/DROPBOX/dropbox_log.log &
