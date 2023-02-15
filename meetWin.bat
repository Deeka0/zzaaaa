@echo off
setlocal enableDelayedExpansion

set /p asker="How many users would you like to create?: "

for /l %%x in (1,1,%asker%) DO (wt -w 0 nt cmd /k "python C:\Games\zzWin-main\zoom.py")

