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
