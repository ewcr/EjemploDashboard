call "C:\pyvenv\3.12.10\streamlit\Scripts\activate"
pip install --upgrade pyinstaller
pyinstaller --onefile --icon="icono.ico" main.py
pause