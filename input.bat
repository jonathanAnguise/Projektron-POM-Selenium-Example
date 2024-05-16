@echo off

REM Activate the virtual environment
start cmd /k venv\Scripts\activate.bat && python3 main.py hours=9 minutes=0 title=TA reference=TA task_description="My_task_description"