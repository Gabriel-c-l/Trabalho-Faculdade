# Conversor de Bases Numéricas

Este repositório contém uma versão principal em Python e uma versão visual opcional.
Não há bibliotecas de terceiros; os algoritmos foram implementados manualmente.

As duas formas de uso são:

- `py/main.py` — menu interativo em console.
- `web/index.html` — interface visual com CSS separado para edição fácil.

## Alinhamento com o enunciado

O trabalho atende ao tema de **conversão de sistemas numéricos / mudança de base**.

- A lógica de conversão foi feita manualmente, sem funções prontas de conversão.
- A versão em `py/main.py` é a mais segura para a entrega, porque está em **Python** e usa apenas recursos nativos.
- A versão visual em `web/` é um bônus de apresentação. Se o professor exigir que tudo fique só em Python ou Java, apresente a versão de console como principal.

## O que precisa ter instalado

- **Python 3** para rodar a versão de console e os testes.
- **Um navegador** para abrir a versão visual.

Não é necessário instalar pacotes com `pip`.

Estrutura principal:

- `py/conversor.py` — funções de conversão e validação.
- `py/main.py` — menu interativo no console.
- `py/tests/test_conversor.py` — testes simples executáveis.
- `web/index.html` — interface visual em HTML.
- `web/style.css` — aparência da interface, fácil de alterar.
- `web/script.js` — lógica da versão visual.
- `run_python.bat` — script para executar a versão console em nova janela.
- `run_app.bat` — script para abrir a versão visual no navegador.
- `entrega/listagem_programa.md` — documento de entrega com a listagem e explicação do programa.
- `entrega/roteiro_apresentacao.md` — roteiro curto para a apresentação.

## Como executar

1. Abrir terminal na pasta do projeto:

```powershell
cd "C:\Users\Gabriel.lopes\Desktop\Calculadora java"
```

2. Abrir a interface visual no navegador:

```powershell
.\run_app.bat
```

Se preferir, também dá para abrir direto no navegador com um duplo clique em `web/index.html`.

3. Se quiser a versão console ou os testes, use o launcher de texto:

```powershell
.\run_python.bat
```

4. No menu escolha `1` para rodar o menu interativo ou `2` para rodar os testes.

Se o Windows não reconhecer o comando `python`, troque por `py -3` dentro do arquivo `run_python.bat`.

## Rodar direto sem os arquivos `.bat`

Na pasta `py`, rode o menu principal com:

```powershell
python main.py
```

Ou rode os testes com:

```powershell
python -m tests.test_conversor
```

## Observações importantes

- Suporta números inteiros, inclusive negativos. A parte fracionária não está implementada.
- A interface visual usa apenas HTML, CSS e JavaScript puro.
- Sua colega pode mexer no visual alterando principalmente `web/style.css`.
- Mensagens de erro são exibidas para entradas inválidas; você pode tentar novamente no menu.

## Arquivos de entrega

Se o professor pedir o material para enviar, os arquivos principais já estão separados na pasta `entrega/`.
