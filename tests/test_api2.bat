

@echo off
echo Send to the server...

curl -X POST http://127.0.0.1:5000/add_produs/ ^
     -H "Content-Type: application/json" ^
     -d "{\"name\":\"pen\", \"price\":20}"

echo.
echo Operatiune finalizata.
pause