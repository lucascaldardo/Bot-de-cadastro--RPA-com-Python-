# Bot de cadastro (RPA com Python)
O script lê um arquivo CSV (`produtos.csv`) e preenche automaticamente o formulário de cadastro usando **PyAutoGUI** para simular cliques e digitação + **Pandas** para ler os dados.

### Funcionalidades
- Abre o Chrome e acessa o sistema
- Realiza login automático
- Cadastra cada produto do CSV (código, marca, tipo, categoria, preço, custo, observação)
- Trata campos opcionais (obs)

### Tecnologias usadas
- Python
- PyAutoGUI (automação de mouse/teclado)
- Pandas (leitura de CSV)

### Como usar
1. Tenha o arquivo `produtos.csv` na pasta certa (ajuste o caminho no código)
2. Ajuste as coordenadas de clique conforme sua tela (use `pyautogui.position()` para descobrir)
3. Rode o script: `python bot_cadastro.py`

**Atenção**: Este bot usa coordenadas fixas de tela → funciona melhor em resolução e setup idênticos ao de desenvolvimento. Para versões mais robustas, considere Selenium ou image recognition, esse projeto foi feito na jornada Python da hashtag.