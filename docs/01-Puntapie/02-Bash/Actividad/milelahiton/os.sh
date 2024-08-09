#!/bin/bash

SO=$(lsb_release -sd)
Kernel=$(uname -r)
CPU=$(lscpu | sed -nr '/Model name/ s/.*:\s*(.*) @ .*/\1/p')
Ram=$(cat /proc/meminfo | awk '/MemTotal/ { printf "%3.2f \n" , $2/1024/1024}' /proc/meminfo)
Python=$(python3 -V)

echo ""sistema_operativo": $SO"
echo ""kernel": $Kernel"
echo ""cpu": $CPU"
echo ""memoria_total": $Ram"GB""
echo ""version_bash:" $BASH_VERSION"
echo ""version_python:" $Python"