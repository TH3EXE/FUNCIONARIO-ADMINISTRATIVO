@echo off
setlocal
color 0E
title Contratando - FUNCIONARIO ADMINISTRATIVO

echo ======================================================
echo  Bem-vindo, novo FUNCIONARIO ADMINISTRATIVO!
echo ======================================================

REM Variaveis de configuracao
set PYTHON_VERSION=3.10.11
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%
set DEPENDENCIAS=pandas openpyxl unidecode colorama pyperclip

echo.
echo [1/4] Verificando privilegios de administrador...
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Por favor, execute este arquivo como Administrador.
    echo Clique com o botao direito no arquivo e selecione "Executar como administrador".
    goto end
)

echo.
echo [2/4] Verificando a instalacao do Python...

REM Verifica se o Python ja esta instalado na versao desejada
python --version 2>nul | findstr /i "%PYTHON_VERSION%" >nul
if %errorlevel% equ 0 (
    echo.
    echo Python %PYTHON_VERSION% ja esta instalado. Pulando a instalacao.
) else (
    echo.
    echo Python nao detectado ou versao incorreta. Iniciando a instalacao...
    echo Baixando o instalador do Python...
    
    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_DOWNLOAD_URL%' -OutFile '%PYTHON_INSTALLER%'"
    
    if %errorlevel% neq 0 (
        echo.
        echo ERRO: Falha ao baixar o instalador do Python. Verifique sua conexao com a internet.
        goto end
    )
    
    echo.
    echo Executando instalacao silenciosa do Python. Por favor, aguarde...
    echo Esta etapa pode demorar alguns minutos.
    
    REM Executa a instalacao silenciosa e adiciona ao PATH
    start /wait "" "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1
    
    if %errorlevel% neq 0 (
        echo.
        echo ERRO: A instalacao do Python falhou.
        goto end
    )
    
    echo.
    echo Instalacao do Python concluida com sucesso!
)

REM Recarrega o PATH para a sessao atual do prompt
set PATH=%PATH%;%APPDATA%\Python\Python310\Scripts\
set PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python310\Scripts\

echo.
echo [3/4] Instalando as dependencias do codigo...

REM Instala as bibliotecas usando o pip de forma robusta
pip install --no-cache-dir %DEPENDENCIAS%
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha ao instalar as dependencias. Verifique a conexao com a internet.
    goto end
)

echo.
echo [4/4] Verificando a instalacao das dependencias...

REM Verifica se todas as dependencias foram instaladas
for %%a in (%DEPENDENCIAS%) do (
    pip show %%a >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao instalar a dependencia: %%a.
        goto end
    )
)

echo.
echo ======================================================
echo  Instalacao completa!
echo  Voce ja pode executar o seu script.
echo ======================================================

:end
echo.
pause
endlocal