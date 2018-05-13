Cerca l'errore
==============

Esercizio da svolgere
+++++++++++++++++++++

Cerca gli errori in questo script::

  names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve']
  ages = [22, 32, 18, 57, 41]
  current_year = 2017

  for person in range(6)
      age = ages(person)
      name = names[person]
      year_of_birth = age - current_year
      print('name' + ' was born in ' + year_of_birth)

Ecco la correzione::

  names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve']
  ages = [22, 32, 18, 57, 41]
  current_year = 2017

  for person in range(0,6)
        age = ages[person]
        name = names[person]
        year_of_birth = current_year - age
        print(name + ' was born in ' + str(year_of_birth))
