#!/bin/bash
source bin/activate

if [ -z "$1" ]; then
    echo "Error: Bot name argument provided." >&2
	echo "Usage: ./start <bot name> <chanel name>"
    exit 1
fi
if [ -z "$2" ]; then
    echo "Error:Channel name not provided." >&2
	echo "Usage: ./start <bot name> <chanel name>"
    exit 1
fi


node twitch-chat-logger.js $1 $2
