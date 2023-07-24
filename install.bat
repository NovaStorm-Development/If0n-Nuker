@echo off
color 04
pip install discord

set /p Choice=Do you want to run the builder? Y or N
if %Choice% == Y goto BUILDER
if %Choice% == N goto DONE


:BUILDER
python builder.py

:DONE
Done