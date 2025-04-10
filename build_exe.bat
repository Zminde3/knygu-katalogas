@echo off
call .venv\Scripts\activate.bat
pyinstaller --noconfirm --onefile ^
--add-data "book_catalog\\templates;book_catalog\\templates" ^
--add-data "book_catalog\\static;book_catalog\\static" ^
--add-data "book_catalog\\books.db;book_catalog" ^
book_catalog/run.py
pause
