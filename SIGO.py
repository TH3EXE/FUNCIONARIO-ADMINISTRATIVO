import pyautogui
import time
import sys
import pyperclip


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
    print("Você tem 10 segundos para copiar os dados e pressionar Enter.")

    input("Pressione Enter após copiar os dados para o clipboard...")
    time.sleep(1)  # Pequena pausa para garantir que o clipboard foi atualizado

    try:
        dados_str = pyperclip.paste().strip()
        dados_lista = dados_str.splitlines()

        # Garante que o número de campos está correto
        if len(dados_lista) != 6:
            raise ValueError(
                "O formato dos dados está incorreto. Certifique-se de que são 6 campos em linhas separadas.")

        procedimento, cnpj, crm, qt_autoriz, observacao, telefone = dados_lista

        print("\nDados lidos do clipboard com sucesso:")
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
        print(f"Erro ao ler os dados do clipboard: {e}")
        return None


def selecionar_aba_secundaria():
    """
    Seleciona a aba "Aut. Procedimento" antes de iniciar a automação.
    As coordenadas foram fornecidas pelo usuário.
    """
    print("Selecionando a aba correta do sistema...")
    pyautogui.click(x=294, y=1008)
    time.sleep(1)
    pyautogui.click(x=691, y=156)
    time.sleep(1)


def preencher_formulario(dados):
    """
    Automatiza o preenchimento do formulário com os dados fornecidos.
    """
    print("Você tem 5 segundos para clicar na janela do sistema...")
    time.sleep(0.2)

    print("Iniciando o preenchimento automático. NÃO TOQUE NO MOUSE OU TECLADO.")

    try:
        try:
            janela = pyautogui.getWindowsWithTitle('NOTRE DAME INTERMEDICA SAUDE S A')[0]
            if janela.isMinimized:
                janela.restore()
            janela.activate()
            window_x, window_y = janela.topleft
        except IndexError:
            print("Janela do NOTRE DAME não encontrada. Certifique-se de que está aberta.")
            return

        pyautogui.click(x=window_x + 33, y=window_y + 276)
        pyautogui.write("N")
        pyautogui.press("tab")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 245, y=window_y + 277)
        pyautogui.write("AUTO DIGITAL")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 48, y=window_y + 313)
        pyautogui.write(dados["procedimento"])
        pyautogui.press("tab")
        time.sleep(1)

        # Captura o texto do campo para verificar se já existe um CID.
        pyautogui.click(x=window_x + 755, y=window_y + 311)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1) #Tempo para copiar a informação
        texto_cid = pyperclip.paste()
        pyautogui.press("tab")

        # Verifica se o campo de CID está vazio
        if not texto_cid or texto_cid.isspace():
            print("Campo CID não preenchido. Preenchendo com Z000.")
            pyautogui.write("Z000")
            pyautogui.press("tab")
        else:
            print(f"Campo CID já preenchido com '{texto_cid}'. Ignorando.")

        pyautogui.click(x=window_x + 785, y=window_y + 310)
        pyautogui.write("1")
        pyautogui.press("tab")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 112, y=window_y + 400)
        pyautogui.write("0")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 141, y=window_y + 397)
        pyautogui.write("2")
        pyautogui.press("tab")
        pyautogui.write(dados["cnpj"])
        time.sleep(0.1)

        pyautogui.click(x=window_x + 663, y=window_y + 402)
        pyautogui.write(dados["crm"])
        time.sleep(0.1)

        pyautogui.click(x=window_x + 368, y=window_y + 444)
        pyautogui.write("AUTO DIGITAL")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 35, y=window_y + 480)
        pyautogui.write(dados["qt_autoriz"])
        time.sleep(0.1)

        pyautogui.click(x=window_x + 37, y=window_y + 515)
        pyautogui.write(dados["observacao"])
        time.sleep(0.1)

        pyautogui.click(x=window_x + 96, y=window_y + 588)
        pyautogui.write("Beneficiario")
        time.sleep(0.1)

        pyautogui.click(x=window_x + 305, y=window_y + 587)
        pyautogui.write(dados["telefone"])
        time.sleep(0.1)

        print("Preenchimento concluído com sucesso!")
        time.sleep(2)

    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")
        print("Verifique se a janela do sistema está ativa.")


if __name__ == "__main__":
    while True:
        dados_preencher = obter_dados_do_clipboard()

        if dados_preencher:
            selecionar_aba_secundaria()
            preencher_formulario(dados_preencher)

        continuar = input("Autorização concluída. Deseja fazer uma nova? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o script...")
            break