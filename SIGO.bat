@echo off
setlocal
echo Preparando o ambiente para a automacao...

:: Define o caminho exato fornecido pelo usuario
set "DOCS_PATH=C:\Users\marcos.oliveira7\Documents"

:: Cria a pasta "SIGO" se ela nao existir
if not exist "%DOCS_PATH%\SIGO" (
    mkdir "%DOCS_PATH%\SIGO"
    echo Pasta 'SIGO' criada em Documentos.
)

:: Entra na pasta criada
cd /d "%DOCS_PATH%\SIGO"

echo Criando o arquivo Python...
(
echo import pyautogui
echo import time
echo.
echo def autorizacao_sigo_automatico(procedimento, cnpj, crm, qt_autoriz, observacao, telefone):
echo     """
echo     Funcao para automatizar o preenchimento no sistema Oracle Forms.
echo     As coordenadas X,Y devem ser ajustadas para a sua tela.
echo     """
echo.
echo     try:
echo         janela = pyautogui.getWindowsWithTitle('Oracle Developer Forms Runtime - Web')[0]
echo         if janela.isMinimized:
echo             janela.restore()
echo         janela.activate()
echo     except IndexError:
echo         print("Janela do Oracle Forms nao encontrada. Certifique-se de que esta aberta.")
echo         return
echo.
echo     print("Iniciando a automacao...")
echo     time.sleep(2)
echo.
echo     pyautogui.click(x=350, y=250)
echo     pyautogui.write("N")
echo     pyautogui.press("tab")
echo     time.sleep(0.5)
echo.
echo     pyautogui.click(x=350, y=300)
echo     pyautogui.write("AUTO DIGITAL")
echo     time.sleep(0.5)
echo.
echo     pyautogui.click(x=350, y=400)
echo     pyautogui.write(procedimento)
echo     pyautogui.press("tab")
echo     time.sleep(1)
echo.
echo     pyautogui.click(x=350, y=450)
echo     pyautogui.write("Z000")
echo.
echo     pyautogui.click(x=350, y=500)
echo     pyautogui.write("1")
echo     pyautogui.press("tab")
echo.
echo     pyautogui.click(x=350, y=550)
echo     pyautogui.write("2")
echo     pyautogui.press("tab")
echo     pyautogui.write(cnpj)
echo.
echo     pyautogui.click(x=350, y=650)
echo     pyautogui.write(crm)
echo.
echo     pyautogui.click(x=350, y=700)
echo     pyautogui.write("AUTO DIGITAL")
echo.
echo     pyautogui.click(x=350, y=750)
echo     pyautogui.write(qt_autoriz)
echo.
echo     pyautogui.click(x=350, y=800)
echo     pyautogui.write(observacao)
echo.
echo     pyautogui.click(x=850, y=250)
echo     pyautogui.write("Beneficiario")
echo.
echo     pyautogui.click(x=850, y=300)
echo     pyautogui.write(telefone)
echo.
echo     print("Preenchimento dos campos concluido!")
echo.
echo     procedimento_cod = "20103492"
echo     cnpj_prestador = "11941449152"
echo     crm_solicitante = "1UXPX007099002"
echo     qt_autorizada = "1"
echo     observacao_form = "Automação via script Python"
echo     telefone_beneficiario = "80071104"
echo.
echo     autorizacao_sigo_automatico(
echo         procedimento=procedimento_cod,
echo         cnpj=cnpj_prestador,
echo         crm=crm_solicitante,
echo         qt_autoriz=qt_autorizada,
echo         observacao=observacao_form,
echo         telefone=telefone_beneficiario
echo     )
) > autorizacao_sigo.py

echo Arquivo 'autorizacao_sigo.py' criado com sucesso.

echo.
echo Instalando dependencias. Isso pode demorar um pouco...
pip install pyautogui
pip install opencv-python

echo.
echo ==========================================================
echo A automacao foi criada e as dependencias foram instaladas!
echo ==========================================================
echo.
echo Proximos passos:
echo 1. Navegue ate a pasta "C:\Users\marcos.oliveira7\Documents\SIGO".
echo 2. Abra o arquivo "autorizacao_sigo.py" com o Bloco de Notas ou um editor de codigo.
echo