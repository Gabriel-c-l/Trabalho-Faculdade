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
