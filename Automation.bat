@echo off

REM Navigate to the folder where your files are located
cd "D:\Dell"

REM Run the AutoHotkey script
REM start "" "Script - Shortcut.lnk"
REM timeout /t 5 /nobreak >nul

REM Run the first Python script and wait for it to finish
start /wait python "Fetch.exe"

REM Run the second Python script and wait for it to finish
start /wait python "toCSVfetch.py"

REM Run the third Python script and wait for it to finish
start /wait python "toCSVcmd.py"

REM Run the fourth Python script and wait for it to finish
start /wait python "merge.py"

REM Run the fifth Python script and wait for it to finish
start /wait python "set.py"

REM Run the sixth Python script and wait for it to finish
start /wait python "main.py"


REM Run the seventh Python script and wait for it to finish
start /wait python "final.py"


REM Run the eighth Python script and wait for it to finish
start /wait python "normalize.py"


REM Run the nininth Python script and wait for it to finish
start /wait python "recommendation.py"



REM Run the tenth Python script and wait for it to finish
start /wait python "stat.py"

REM Run the gui Python script and wait for it to finish
start /wait python "gui1.py"

REM Run the nininth Python script and wait for it to finish
start /wait python "try.py"


REM Close all remaining command prompt windows
taskkill /F /IM cmd.exe

exit
