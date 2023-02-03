import eel
from logic.compiler import Compiler

class MainWindow:

    def __init__(self):
        self.compiler = Compiler()
        eel.init("web")
        self.Launch()

    @eel.expose
    def Launch(self):
        eel.start("index.html")


if __name__ == "__main__":
    MainWindow()