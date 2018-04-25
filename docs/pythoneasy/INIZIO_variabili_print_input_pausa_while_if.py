from time import sleep
valore=10

print ('ciao')

while valore < 100:
  print (valore)
  valore += 10
  sleep(0.1)

print("terminato")

if valore < 10: # la verifica viene eseguita una volta sola
    print("valore è minore di 10")
elif valore < 20:
    print("valore è minore di 20 ma non di 10")
elif valore == 100:
    print("valore è uguale a 100")

nome = input('Come ti chiami? ')
print ('Ciao '+nome+'.')

anni = input('Quanti anno hai? ')
print (str(anni)+' anni non sono molti')
