#!/bin/bash
#Read user input to know how many instance of the zoom meeting to run.
echo "How many users would you like to create?"
read users
for i in $(seq $users)
do
  echo ${BASH_VERSION}
  osascript -e 'tell application "Terminal" to activate' \
  -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' \
  -e 'tell application "Terminal" to do script "python3 /Users/dark/Desktop/zzAll/zoom.py" in selected tab of the front window'
  
  #osascript -e 'tell application "Terminal" to do script "python3 /Path-to-working-directory/zoom.py"'
  #osascript -e "do shell script \"osascript -e \\\"tell application \\\\\\\"Terminal\\\\\\\" to quit\\\" &> /dev/null &\""; exit
  #sleep 5
done

