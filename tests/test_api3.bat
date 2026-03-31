

@echo off

@echo Send to the Server...

curl -X POST http://127.0.0.1:5000/add_produs/ \
     -H "Content-Type: application/json" \
     -d '{"name":"printer","price":200}'

echo.
echo Operatiune finalizata.
pause