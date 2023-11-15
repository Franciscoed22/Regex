#importar biblioteca de expressões regulares
import re
expr = re.compile(r"^\s*([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})\s*$")

#insere um CPF
cpf = input("Digite um CPF: ")

#caso seja válido aplicar mascara de formato cpf
if expr.search(cpf):
    cpfComSimbol = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    print(f"{cpfComSimbol} é válido")
else:
    print(f"{cpf} é inválido")