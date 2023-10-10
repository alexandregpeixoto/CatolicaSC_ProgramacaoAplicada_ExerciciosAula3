# Entra com a palavra ou texto
texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
# Atribui na lista removendo os espaços vazios
lista = [caracter for caracter in texto if caracter != ' ']
# Cria uma nova lista e armazena a lista anterior invertida
listaInvertida = lista[::-1]
# Compara as duas listas
if lista == listaInvertida:
    print(f'A entrada "{texto}" é um palíndromo.')
else:
    print(f'A entrada "{texto}" não é um palíndromo.')