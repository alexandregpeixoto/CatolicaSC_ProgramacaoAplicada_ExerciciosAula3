import string
# Entra com a palavra ou texto
texto = input("Digite uma palavra ou texto: ")
# Remove toda a pontuação
texto = texto.translate(str.maketrans("","",string.punctuation))
# Solicita o valor de repetição
repeticoesDesejadas = int(input("Quantas vezes a palavra deve aparecer? "))

palavras = texto.split()
dicionarioRecorrencia = {}

for palavra in palavras:
    if palavra in dicionarioRecorrencia:
        dicionarioRecorrencia[palavra] += 1
    else:
        dicionarioRecorrencia[palavra] = 1

for palavra, repeticoesEncontradas in dicionarioRecorrencia.items():
    if repeticoesEncontradas >= repeticoesDesejadas:
        print(f"{palavra}, {repeticoesEncontradas}")
