@echo off
FOR /f “tokens=2 delims=:” %%G IN (‘netsh wlan show profile ^| find “All User Profile” ‘) DO (call :trim %%G )

GOTO :eof

:trim
echo %*
netsh wlan show profile name=”%*” key=clear | find “Key Content”
GOTO :eof