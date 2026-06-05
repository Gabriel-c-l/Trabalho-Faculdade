@echo off
REM Launcher para abrir a versão visual em HTML/CSS/JS
setlocal
set "WEB_INDEX=%~dp0web\index.html"

echo Abrindo a interface visual do Conversor...
start "" "%WEB_INDEX%"

endlocal
exit /b 0
