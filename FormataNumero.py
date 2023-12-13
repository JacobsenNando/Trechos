import re

def format_number(num):
    # Remover não dígitos
    num_digits = re.sub(r'[^\d]', '', num)

    if len(num_digits) >= 8 and num_digits[-8] not in ['2', '3', '0']:
        # Adicionar o código internacional '55', '9' antes dos 8 últimos dígitos
        formatted_num = '55' + num_digits[:2]+ '9' + num_digits[-8:]
        return formatted_num
    else:
        # Se o oitavo dígito (contando de trás para frente) for 2, 3 ou 0, passar no filtro sem alteração
        return "55" + num_digits

# Exemplo de uso
numeros = [
    "(51)995553103",
    "(51)9922-7008",
    "(51)99661-2796",
    "51996168081",
    "(55)3114-1541",
    "(55)2182-7159"
]

for numero in numeros:
    numero_formatado = format_number(numero)
    print(numero_formatado)
