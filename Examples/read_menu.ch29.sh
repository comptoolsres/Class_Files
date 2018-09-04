#!/bin/bash
# while-menu: a menu driven system information program

DELAY=3 # Number of seconds to display results
while [[ "$REPLY" != 0 ]]; do
    clear # clear the screen

    # Display the menu to the user
    cat <<- _EOF_
        Please Select:
        1. Display System Information
        2. Display Disk Space
        3. Display Home Space Utilization
        0. Quit
_EOF_
 
    read -p "Enter selection [0-3] > " # Get input from user
    if [[ "$REPLY" =~ ^[0-3]$ ]]; then # If REPLY is between 0-3
        if [[ $REPLY == 1 ]]; then # If REPLY is 1
            echo "Hostname: $HOSTNAME" 
            uptime
            sleep "$DELAY"
        fi
        if [[ "$REPLY" == 2 ]]; then # If REPLY is 2
            df -h
            sleep "$DELAY"
        fi
        if [[ "$REPLY" == 3 ]]; then # If REPLY is 3
            if [[ "$(id -u)" -eq 0 ]]; then # If the user is root (id 0)
                echo "Home Space Utilization (All Users)"
                du -sh /home/*
            else # If user is not root
                echo "Home Space Utilization ($USER)"
                du -sh "$HOME"
            fi
            sleep "$DELAY"
        fi
    else # REPLY is not 0-3
        echo "Invalid entry."
        sleep "$DELAY"
    fi
done
echo "Program terminated."
