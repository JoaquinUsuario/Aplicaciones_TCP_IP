#!/bin/bash

fecha=$(date)

while read -r RENGLON; do
    resp=$(curl -sL -w "%{http_code}\n" "$RENGLON" -o /dev/null)
    if [ "$resp" -eq "200" ]
    then
        estado="UP!"
    else
        estado="DOWN!"
    fi
    echo "$fecha - $RENGLON - $resp - $estado"
done < "$1"