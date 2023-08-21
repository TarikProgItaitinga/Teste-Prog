meuNumero = int(input(f"Digite um número:"))

for i in range(1,11):
    print(meuNumero,"x",i,"=",meuNumero*i) #Método tradicional

    print(f"{meuNumero} x {i} = {meuNumero*i}") #Método com formatação