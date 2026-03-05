

@echo off
echo Trimitem datele catre server...

curl -X POST http://127.0.0.1:5000/add_produs/ ^
     -H "Content-Type: application/json" ^
     -d "{\"nume\":\"Printer\", \"pret\":200}"

echo.
echo Operatiune finalizata.
pause