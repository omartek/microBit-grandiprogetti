from guizero import App, PushButton, Slider
app = App()

# a PushButton's size is noted in characters
button = PushButton(app)
button.width = 30
button.height = 5

# a Slider's size is noted in pixels
slider = Slider(app)
slider.width = 300
slider.height = 30

app.display()
