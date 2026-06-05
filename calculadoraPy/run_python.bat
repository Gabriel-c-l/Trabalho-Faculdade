@echo off
REM Script para executar a versão Python do Conversor no console
setlocal
cd /d "%~dp0\py"

echo Escolha:
echo 1) Executar menu interativo (main.py)
echo 2) Executar testes (tests\test_conversor.py)
echo 0) Sair
set /p CHOICE=Escolha (1/2/0): 
if "%CHOICE%"=="1" goto RUN_MAIN
if "%CHOICE%"=="2" goto RUN_TESTS
goto END

:RUN_MAIN
echo Abrindo janela para o programa (permanece aberta)...
start "Conversor-Python" cmd /k "python main.py"
goto END

:RUN_TESTS
echo Abrindo janela para testes (permanece aberta)...
start "Conversor-Tests" cmd /k "python -m tests.test_conversor & pause"
goto END

:END
endlocal
exit /b 0
