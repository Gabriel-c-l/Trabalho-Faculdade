# Listagem do Programa

Tema: Conversão de sistemas numéricos / mudança de base

Este documento reúne a estrutura principal do trabalho e os arquivos usados na entrega.

## Estrutura do projeto

- `py/conversor.py` - contém toda a lógica manual de conversão e validação.
- `py/main.py` - menu interativo em console para demonstrar o trabalho.
- `py/tests/test_conversor.py` - testes simples de validação das funções.
- `web/index.html` - interface visual alternativa para apresentação.
- `web/style.css` - estilos da interface visual, separados para facilitar edição.
- `web/script.js` - lógica da interface visual.
- `run_python.bat` - atalho para abrir o menu de console ou os testes.
- `run_app.bat` - atalho para abrir a interface visual no navegador.

## Observação técnica

O professor pediu um software matemático sem uso de bibliotecas prontas para resolver o tema. A lógica de conversão foi feita manualmente com operações básicas de divisões sucessivas e leitura de dígitos.

## Código principal

### `py/conversor.py`

```python
"""
Conversor de bases numéricas (sem bibliotecas externas).
Implementa decimal<->bin/oct/hex com algoritmos manuais.
"""

HEX_DIGITS = "0123456789ABCDEF"


def dec_para_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    sinal = ""
    valor = n
    if valor < 0:
        sinal = "-"
        valor = -valor
    restos = []
    while valor > 0:
        resto = valor % base
        if base == 16:
            restos.append(HEX_DIGITS[resto])
        else:
            restos.append(str(resto))
        valor //= base
    restos.reverse()
    return sinal + ''.join(restos)


def dec_para_binario(n: int) -> str:
    return dec_para_base(n, 2)


def dec_para_octal(n: int) -> str:
    return dec_para_base(n, 8)


def dec_para_hexadecimal(n: int) -> str:
    return dec_para_base(n, 16)


def digito_para_valor(c: str) -> int:
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    up = c.upper()
    if 'A' <= up <= 'F':
        return 10 + ord(up) - ord('A')
    return -1


def base_para_decimal(s: str, base: int) -> int:
    if s is None:
        raise ValueError('Entrada vazia')
    t = s.strip()
    if t == '':
        raise ValueError('Entrada vazia')
    negativo = False
    if t[0] in '+-':
        if t[0] == '-':
            negativo = True
        t = t[1:]
    if t == '':
        raise ValueError('Entrada inválida')
    resultado = 0
    for ch in t:
        v = digito_para_valor(ch)
        if v < 0 or v >= base:
            raise ValueError(f"Caractere inválido para base {base}: '{ch}'")
        resultado = resultado * base + v
        if resultado > 2**31 - 1:
            raise ValueError('Overflow: valor excede intervalo suportado (int 32-bit)')
    return -resultado if negativo else resultado


def binario_para_decimal(s: str) -> int:
    return base_para_decimal(s, 2)


def octal_para_decimal(s: str) -> int:
    return base_para_decimal(s, 8)


def hexadecimal_para_decimal(s: str) -> int:
    return base_para_decimal(s, 16)


def validar_binario(s: str) -> bool:
    if s is None:
        return False
    t = s.strip()
    if t == '':
        return False
    if t[0] in '+-':
        t = t[1:]
    return all(c in '01' for c in t)


def validar_octal(s: str) -> bool:
    if s is None:
        return False
    t = s.strip()
    if t == '':
        return False
    if t[0] in '+-':
        t = t[1:]
    return all('0' <= c <= '7' for c in t)


def validar_hex(s: str) -> bool:
    if s is None:
        return False
    t = s.strip()
    if t == '':
        return False
    if t[0] in '+-':
        t = t[1:]
    return all(('0' <= c <= '9') or ('A' <= c.upper() <= 'F') for c in t)


if __name__ == '__main__':
    # Quick manual test
    print('13 -> bin:', dec_para_binario(13))
    print('255 -> hex:', dec_para_hexadecimal(255))
    print('1010 -> dec:', binario_para_decimal('1010'))
```

### `py/main.py`

```python
"""
Menu interativo em console para o conversor em Python.
"""

from conversor import (
    dec_para_binario,
    dec_para_octal,
    dec_para_hexadecimal,
    binario_para_decimal,
    octal_para_decimal,
    hexadecimal_para_decimal,
    validar_binario,
    validar_octal,
    validar_hex,
)


def limpar():
    print('\n' * 40)


def esperar():
    input('\nPressione Enter para voltar ao menu...')


def menu():
    while True:
        limpar()
        print('==============================================')
        print('   Conversor de Bases Numéricas (Python)')
        print('==============================================')
        print('1) Decimal → Binário')
        print('2) Decimal → Octal')
        print('3) Decimal → Hexadecimal')
        print('4) Binário → Decimal')
        print('5) Octal → Decimal')
        print('6) Hexadecimal → Decimal')
        print('0) Sair')
        escolha = input('\nEscolha uma opção: ').strip()

        if escolha == '0':
            print('Encerrando...')
            break

        if escolha in ('1', '2', '3'):
            s = input('Digite número decimal (inteiro): ').strip()
            try:
                n = int(s)
            except ValueError:
                print('Entrada inválida: não é um inteiro decimal.')
                esperar()
                continue
            if escolha == '1':
                print('Resultado:', dec_para_binario(n))
            elif escolha == '2':
                print('Resultado:', dec_para_octal(n))
            else:
                print('Resultado:', dec_para_hexadecimal(n))
            esperar()
            continue

        if escolha in ('4', '5', '6'):
            if escolha == '4':
                s = input('Digite número binário: ').strip()
                if not validar_binario(s):
                    print('Entrada inválida para binário.')
                    esperar()
                    continue
                try:
                    print('Resultado:', binario_para_decimal(s))
                except Exception as e:
                    print('Erro:', e)
                esperar()
                continue

            if escolha == '5':
                s = input('Digite número octal: ').strip()
                if not validar_octal(s):
                    print('Entrada inválida para octal.')
                    esperar()
                    continue
                try:
                    print('Resultado:', octal_para_decimal(s))
                except Exception as e:
                    print('Erro:', e)
                esperar()
                continue

            if escolha == '6':
                s = input('Digite número hexadecimal: ').strip()
                if not validar_hex(s):
                    print('Entrada inválida para hexadecimal.')
                    esperar()
                    continue
                try:
                    print('Resultado:', hexadecimal_para_decimal(s))
                except Exception as e:
                    print('Erro:', e)
                esperar()
                continue

        print('Opção inválida. Tente novamente.')
        esperar()


if __name__ == '__main__':
    menu()
```

### `py/tests/test_conversor.py`

```python
from conversor import (
    dec_para_binario,
    dec_para_hexadecimal,
    binario_para_decimal,
    hexadecimal_para_decimal,
    octal_para_decimal,
)


def testar(nome, esperado, atual):
    if str(esperado) == str(atual):
        print(f"{nome}: PASS")
    else:
        print(f"{nome}: FAIL (esperado={esperado}, atual={atual})")


def main():
    testar('dec->bin 13', '1101', dec_para_binario(13))
    testar('dec->hex 255', 'FF', dec_para_hexadecimal(255))
    testar('bin->dec 1010', 10, binario_para_decimal('1010'))
    testar('hex->dec FF', 255, hexadecimal_para_decimal('FF'))
    testar('oct->dec 17', 15, octal_para_decimal('17'))
    print('Teste finalizado.')


if __name__ == '__main__':
    main()
```

## Como apresentar

1. Mostrar o tema escolhido.
2. Explicar que a conversão foi feita manualmente, sem bibliotecas prontas.
3. Demonstrar uma conversão decimal para outra base.
4. Demonstrar uma conversão de outra base para decimal.
5. Abrir a versão visual e mostrar que o CSS pode ser alterado facilmente.
6. Mostrar os testes básicos executados com sucesso.
