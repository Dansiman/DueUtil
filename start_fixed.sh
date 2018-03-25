#!/bin/sh
until python run.py; do
    echo "Script 'run.py' crashed with exit code $?.  Respawning.." >&2
    sleep 1
done
