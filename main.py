import eel

@eel.expose
def Launch():
    eel.start("index.html")

if __name__ == "__main__":
    eel.init("web")
    Launch()