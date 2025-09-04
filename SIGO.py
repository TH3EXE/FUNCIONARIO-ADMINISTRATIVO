import pyautogui
import time
import sys


def obter_dados_do_terminal():
    """Solicita e coleta os dados a serem preenchidos no sistema."""
    print("--- Início do preenchimento ---")
    print("Por favor, informe os dados solicitados abaixo:")

    procedimento = input("Digite o código do Procedimento: ")
    cnpj = input("Digite o CNPJ do Prestador: ")
    crm = input("Digite o CRM do Solicitante: ")
    qt_autoriz = input("Digite a Quantidade de autorizações: ")
    observacao = input("Digite a Observação: ")
    telefone = input("Digite o Fone do Beneficiário: ")

    return {
        "procedimento": procedimento,
        "cnpj": cnpj,
        "crm": crm,
        "qt_autoriz": qt_autoriz,
        "observacao": observacao,
        "telefone": telefone,
    }


def selecionar_aba_secundaria():
    """
    Seleciona a aba "Aut. Procedimento" antes de iniciar a automação.
    As coordenadas foram fornecidas pelo usuário.
    """
    print("Selecionando a aba correta do sistema...")
    # Clica na aba principal T22A3S (coordenada da aba no sistema)
    pyautogui.click(x=294, y=1008)
    time.sleep(1) # Pequena pausa para o sistema carregar a aba
    # Clica na aba secundária "Aut. Procedimento" (coordenada da aba secundária)
    pyautogui.click(x=691, y=156)
    time.sleep(1) # Pequena pausa para o sistema carregar a nova tela


def preencher_formulario(dados):
    """
    Automatiza o preenchimento do formulário com os dados fornecidos.

    As coordenadas foram ajustadas com base nas informações que você forneceu.
    """

    # Pausa inicial para você conseguir alternar para a janela do sistema
    print("Você tem 5 segundos para clicar na janela do sistema...")
    time.sleep(5)

    print("Iniciando o preenchimento automático. NÃO TOQUE NO MOUSE OU TECLADO.")

    try:
        # Tenta ativar a janela do sistema usando o nome exato.
        try:
            janela = pyautogui.getWindowsWithTitle('NOTRE DAME INTERMEDICA SAUDE S A')[0]
            if janela.isMinimized:
                janela.restore()
            janela.activate()
            # Obtém a posição da janela na tela
            window_x, window_y = janela.topleft
        except IndexError:
            print("Janela do NOTRE DAME não encontrada. Certifique-se de que está aberta.")
            return

        # --- Coordenadas Relativas (ajustadas a partir do canto da janela) ---

        # Campo "Urgência?"
        pyautogui.click(x=window_x + 33, y=window_y + 276)
        pyautogui.write("N")
        pyautogui.press("tab")
        time.sleep(0.5)

        # Campo "Histórico Clínico"
        pyautogui.click(x=window_x + 245, y=window_y + 277)
        pyautogui.write("AUTO DIGITAL")
        time.sleep(0.5)

        # Campo "Procedimento"
        pyautogui.click(x=window_x + 48, y=window_y + 313)
        pyautogui.write(dados["procedimento"])
        pyautogui.press("tab")
        time.sleep(1)

        # Campo "CID"
        pyautogui.click(x=window_x + 755, y=window_y + 311)
        pyautogui.write("Z000")

        # Campo "Tipo tratamento"
        pyautogui.click(x=window_x + 785, y=window_y + 310)
        pyautogui.write("1")
        pyautogui.press("tab")
        time.sleep(0.5)

        # Campo "Qt. Período"
        pyautogui.click(x=window_x + 112, y=window_y + 400)
        pyautogui.write("0")
        time.sleep(0.5)

        # Campo "Tipo Prestador"
        pyautogui.click(x=window_x + 141, y=window_y + 397)
        pyautogui.write("2")
        pyautogui.press("tab")

        # Campo "CNPJ" (campo seguinte)
        pyautogui.write(dados["cnpj"])
        time.sleep(0.5)

        # Campo "CRM"
        pyautogui.click(x=window_x + 663, y=window_y + 402)
        pyautogui.write(dados["crm"])
        time.sleep(0.5)

        # Campo "Solicitante"
        pyautogui.click(x=window_x + 368, y=window_y + 444)
        pyautogui.write("AUTO DIGITAL")
        time.sleep(0.5)

        # Campo "Qt. autoriz"
        pyautogui.click(x=window_x + 35, y=window_y + 480)
        pyautogui.write(dados["qt_autoriz"])
        time.sleep(0.5)

        # Campo "Observação"
        pyautogui.click(x=window_x + 37, y=window_y + 515)
        pyautogui.write(dados["observacao"])
        time.sleep(0.5)

        # Campo "Tipo (Dados Atendente)"
        pyautogui.click(x=window_x + 96, y=window_y + 588)
        pyautogui.write("Beneficiario")
        time.sleep(0.5)

        # Campo "Fone"
        pyautogui.click(x=window_x + 305, y=window_y + 587)
        pyautogui.write(dados["telefone"])
        time.sleep(0.5)

        print("Preenchimento concluído com sucesso!")
        time.sleep(2)

    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")
        print("Verifique se a janela do sistema está ativa.")


if __name__ == "__main__":
    # 1. Coleta os dados do usuário
    dados_preencher = obter_dados_do_terminal()

    # 2. Inicia o preenchimento automático
    selecionar_aba_secundaria()
    preencher_formulario(dados_preencher)