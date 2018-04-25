import random

nomi=['omar','mario','alberto','giovanni']
aggettivi=['alto','basso','lungo','colorato']

nome_a=random.choice(nomi)
nome_b=random.choice(aggettivi)
num1=random.randint(0,9)
num2=random.randint(0,9)

print (nome_a+nome_b+str(num1)+str(num2))
