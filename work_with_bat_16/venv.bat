@echo off

python -m venv venv

call venv\Scripts\activate.bat

pip install python-docx

pip install pyinstaller