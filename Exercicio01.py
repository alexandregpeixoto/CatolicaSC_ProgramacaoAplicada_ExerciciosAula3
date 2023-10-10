def femeas(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return femeas(numero-1) + femeas(numero-2)


n = int(input("Digite um número:"))
print(f"{femeas(n)}")



