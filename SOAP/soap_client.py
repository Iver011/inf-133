from zeep import Client

client=Client('http://localhost:8000')
result=client.service.Saludar(nombre='Iver')
print(result)
res=client.service.SumaDosNumeros(n1=int(input()),n2=int(input()))
print(res)
res2=client.service.Palindromo(cadena="ojo")
print(res2)