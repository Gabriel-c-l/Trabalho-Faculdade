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
