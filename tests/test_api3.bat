

@echo off
curl -X POST http://127.0.0.1:5000/add_produs/ ^
-d "name=produs&price=10"
pause