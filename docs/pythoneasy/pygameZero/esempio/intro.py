import pgzrun
from random import randint
from time import sleep

WIDTH = 500	# dimesioni della finestra
HEIGHT = 200
cont = 0	# variabile per il conteggio

alien = Actor('alien')
alien.anchor = ('left','top')
print(alien.width, alien.height)
alien_vertici = [[250,100],[250+alien.width,100],
                 [250+alien.width,100-alien.height],[250,100-alien.height]]

RED = 200, 0, 0
BOX = Rect(alien_vertici[0], (alien.width, alien.height)) # oggetto rettangolo

def draw():
    screen.clear()
    screen.fill((255,0,0))
    screen.draw.rect(BOX,RED)
    #screen.draw.circle((20, 20), 20, 'white')
    alien.draw()

def on_mouse_down(pos):     # gestione evento mouse
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
    print(pos)

def update():
    global cont, BOX	# se necessario, importare variabili globali
##    alien.pos = alien_vertici[0] # modifica del valore .topright dello sprite
##    alien.angle += 10
##    alien.left += 2
##    if alien.left > (WIDTH):
##        alien.left = -(alien.width -20)
    BOX = Rect(alien_vertici[cont], (-alien.width, alien.height)) # modifica delle dimensioni del rettangolo
##    sleep(0.5)    # attesa
    if keyboard.left:
##        alien.x -= 1 # modifica negativa della x dello sprite
        alien.right = 250
    elif keyboard.right:
##        alien.x += 1 # modifica positiva della x dello sprite
        alien.left =  250
    elif keyboard.up:
        alien.top = 0 # modifica del top - parte superiore
    elif keyboard.down:
        alien.bottom =  200 # modifica del bottom - parte superiore
    elif keyboard.w:
        alien.pos =  250,100 # posizione definita da .anchor di default è center
    elif keyboard.r:
        x = randint(0,WIDTH) # posizione centrale casuale
        y = randint(0,HEIGHT)
        print(x,y)
        alien.pos = x, y

def pos_casuale():
    global cont
    alien.topright = alien_vertici[cont] # modifica del valore .topright dello sprite
    if cont < 3:    # modifica dell'indice
        cont += 1
    else:
        cont = 0    # azzeramento per evitare chiamate di out_of_range

def pos_casuale2():
    cont_casuale = randint(0,3)
    alien.topright = alien_vertici[cont_casuale]
    print(cont_casuale)

for conta in range(3):
    clock.schedule(pos_casuale, conta)  #azione da eseguire a tempo con schedule

pgzrun.go()
