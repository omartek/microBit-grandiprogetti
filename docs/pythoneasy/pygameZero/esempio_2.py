import pgzrun

def draw():
    screen.clear
    screen.fill((250,0,0))
    screen.draw.text("Text color", (150, 30), color="orange", fontsize=60)
    screen.draw.text("Font name and size", (20, 100), fontname="vera", fontsize=60)
    screen.draw.text("Positioned text", topright=(150, 20))
    screen.draw.text("Allow me to demonstrate wrapped text.", (90, 210), width=180, lineheight=1.5)
    screen.draw.text("Outlined text", (400, 70), owidth=1.5, ocolor=(255,255,0), color=(0,0,0))
    screen.draw.text("Drop shadow", (640, 110), shadow=(2,2), scolor="#202020")
    screen.draw.text("Color gradient", (540, 170), color="red", gcolor="purple")
    screen.draw.text("Transparency", (700, 240), alpha=0.1)
    screen.draw.text("Vertical text", midleft=(40, 440), angle=90)
    screen.draw.text("All together now:\nCombining the above options",
    midbottom=(427,460), width=360, fontname="vera", fontsize=48,
    color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
    
def update():
    pass

pgzrun.go()
