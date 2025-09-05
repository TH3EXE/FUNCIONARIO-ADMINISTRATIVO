import pyautogui
import time
import sys
import pyperclip
from colorama import init, Fore, Style

# Inicializa o Colorama para que as cores funcionem em todos os terminais
init()

# Define os códigos de cor usando a biblioteca Colorama
VERMELHO = Fore.RED
VERDE = Fore.GREEN
AMARELO_BRILHANTE = Fore.YELLOW
FIM = Style.RESET_ALL  # Reseta a cor e formatação


def obter_dados_do_clipboard():
    """
    Coleta os dados a serem preenchidos a partir da área de transferência (clipboard).
    Espera que os dados estejam em formato vertical (um por linha) na seguinte ordem:
    Procedimento
    CNPJ
    CRM
    Qt. Autoriz
    Observacao
    Telefone
    """
    print("--- Início do preenchimento ---")
    print("Por favor, cole os dados no formato vertical (um por linha).")

    input("Pressione Enter após copiar os dados para o clipboard...")
    time.sleep(1)

    try:
        dados_str = pyperclip.paste().strip()
        dados_lista = dados_str.splitlines()

        if len(dados_lista) != 6:
            raise ValueError(
                "O formato dos dados está incorreto. Certifique-se de que são 6 campos em linhas separadas.")

        procedimento, cnpj, crm, qt_autoriz, observacao, telefone = dados_lista

        print(f"{VERDE}\nDados lidos do clipboard com sucesso:{FIM}")
        print(f"1. Procedimento: {procedimento}")
        print(f"2. CNPJ: {cnpj}")
        print(f"3. CRM: {crm}")
        print(f"4. Qt. Autoriz: {qt_autoriz}")
        print(f"5. Observacao: {observacao}")
        print(f"6. Telefone: {telefone}")
        print("-" * 20)

        return {
            "procedimento": procedimento,
            "cnpj": cnpj,
            "crm": crm,
            "qt_autoriz": qt_autoriz,
            "observacao": observacao,
            "telefone": telefone,
        }
    except Exception as e:
        print(f"{VERMELHO}Erro ao ler os dados do clipboard: {e}{FIM}")
        return None


def selecionar_aba_secundaria():
    """
    Seleciona a aba "Aut. Procedimento" antes de iniciar a automação.
    As coordenadas foram fornecidas pelo usuário.
    """
    print("Selecionando a aba correta do sistema...")
    pyautogui.click(x=294, y=1008)
    time.sleep(0.1)
    pyautogui.click(x=691, y=156)
    time.sleep(0.1)


def preencher_formulario(dados):
    """
    Automatiza o preenchimento do formulário com os dados fornecidos.
    Aprimorado para encontrar a janela de forma mais robusta.
    """
    print("Buscando a janela do sistema...")
    janela_encontrada = None
    tempo_limite = 20  # Tempo limite de 20 segundos
    inicio = time.time()

    # Itera sobre todas as janelas ativas
    while not janela_encontrada and (time.time() - inicio) < tempo_limite:
        janelas = pyautogui.getWindowsWithTitle(' ')  # Busca por todas as janelas abertas
        for janela in janelas:
            # Procura por uma parte específica do título
            if 'NOTRE DAME INTERMEDICA' in janela.title.upper():
                janela_encontrada = janela
                break  # Janela encontrada, sai do loop

        if not janela_encontrada:
            time.sleep(1)
            print("Janela não encontrada. Tentando novamente...")

    if not janela_encontrada:
        raise IndexError("A janela do sistema 'NOTRE DAME INTERMEDICA' não foi encontrada após 20 segundos.")

    print("Janela encontrada. Focando...")
    # Ativa a janela, traz para a frente e restaura se estiver minimizada
    if janela_encontrada.isMinimized:
        janela_encontrada.restore()
    janela_encontrada.activate()

    # Obtém as coordenadas do canto superior esquerdo da janela
    window_x, window_y = janela_encontrada.topleft

    print("Iniciando o preenchimento automático. NÃO TOQUE NO MOUSE OU TECLADO.")

    try:
        # Ponto de início da autorização
        pyautogui.click(x=window_x + 33, y=window_y + 276)
        pyperclip.copy("N")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("tab")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 245, y=window_y + 277)
        pyperclip.copy("AUTO DIGITAL")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 48, y=window_y + 313)
        pyperclip.copy(dados["procedimento"])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("tab")
        time.sleep(0.1)

        # Captura o texto do campo para verificar se já existe um CID.
        pyautogui.click(x=window_x + 755, y=window_y + 311)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        texto_cid = pyperclip.paste().strip()
        pyautogui.press("tab")

        if not texto_cid:
            print("Campo CID não preenchido. Preenchendo com Z000.")
            pyperclip.copy("Z000")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("tab")
        else:
            print(f"Campo CID já preenchido com '{texto_cid}'. Ignorando.")

        pyautogui.click(x=window_x + 785, y=window_y + 310)
        pyperclip.copy("1")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("tab")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 112, y=window_y + 400)
        pyperclip.copy("0")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 141, y=window_y + 397)
        pyperclip.copy("2")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("tab")
        pyperclip.copy(dados["cnpj"])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 663, y=window_y + 402)
        pyperclip.copy(dados["crm"])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 368, y=window_y + 444)
        pyperclip.copy("AUTO DIGITAL")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 35, y=window_y + 480)
        pyperclip.copy(dados["qt_autoriz"])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        pyautogui.click(x=window_x + 37, y=window_y + 515)
        pyperclip.copy(dados["observacao"])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        # Clica no campo "Tipo de Contato" para abrir a lista
        pyautogui.click(x=window_x + 96, y=window_y + 588)
        time.sleep(0.1)

        # Navega para a opção "Beneficiário" e a seleciona
        pyautogui.press("down", presses=1)
        pyautogui.press("enter")
        time.sleep(0.1)

        # Preenche o campo de telefone
        pyautogui.click(x=window_x + 305, y=window_y + 587)
        pyperclip.copy(dados["telefone"])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        print(f"{VERDE}Preenchimento concluído com sucesso!{FIM}")
        time.sleep(1)

    except IndexError as e:
        print(f"{VERMELHO}ERRO: {e}{FIM}")
        print("Certifique-se de que a janela do sistema 'NOTRE DAME INTERMEDICA SAUDE S A' está aberta.")
    except Exception as e:
        print(f"{VERMELHO}Ocorreu um erro inesperado durante a automação: {e}{FIM}")
        print("Verifique se a janela do sistema está ativa.")


if __name__ == "__main__":
    contador = 0
    print(f"\n{AMARELO_BRILHANTE}Script de Automação Iniciado!{FIM}\n")
    print("Pressione Ctrl+C a qualquer momento para encerrar.")

    try:
        while True:
            print("\n--- Aguardando novos dados ---")
            dados_preencher = obter_dados_do_clipboard()

            if dados_preencher:
                selecionar_aba_secundaria()
                preencher_formulario(dados_preencher)
                contador += 1

            print("-" * 20)
            print(f"**{AMARELO_BRILHANTE}Autorizações concluídas hoje: {contador}{FIM}**")
            print("Pressione Enter para iniciar a próxima autorização ou Ctrl+C para sair.")
            input()

    except KeyboardInterrupt:
        print(f"\n\n{AMARELO_BRILHANTE}Encerrando o script. Total de autorizações: {contador}{FIM}")
        sys.exit(0)