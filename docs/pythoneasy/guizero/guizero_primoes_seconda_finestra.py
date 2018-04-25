from guizero import App, Window,Text, PushButton, warn,info,error

def open_window():
    window.show(wait=True)
    info("Uh oh!", "You are almost out of biscuits!")

def close_window():
    window.hide()

app = App(title = "Main window")

window = Window(app, title = "2nd window")
window.hide()

open_button = PushButton(app, text = "Open", command = open_window)
close_button = PushButton(window, text = "Close", command = close_window)

app.display()
