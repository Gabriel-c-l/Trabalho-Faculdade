# Conversor (Python)

Como executar:

- Verifique se o Python 3 está instalado e no `PATH`:

```powershell
python --version
```

- Para executar o menu interativo:

```powershell
cd "C:\Users\Gabriel.lopes\Desktop\Faculdade\calculadoraPy\py"
python main.py
```

- Para executar os testes simples inclusos:

```powershell
cd "C:\Users\Gabriel.lopes\Desktop\Faculdade\calculadoraPy\py"
python -m tests.test_conversor
```

- Alternativamente, a partir da pasta raiz do projeto você pode usar o lançador `run_python.bat` e escolher a opção 2.

Dependências:

- Nenhuma biblioteca externa é necessária; o código usa apenas a biblioteca padrão do Python.

Observações:

- Os testes inclusos são um script simples que imprime PASS/FAIL. Para uso profissional, considere migrar para `unittest` ou `pytest`.
