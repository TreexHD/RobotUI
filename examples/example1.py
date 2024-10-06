from robotui.debug import Debug
from robotui.main import TaskHandler
import importlib


def main(console):
    #importlib.reload(module=)
    # use external files
    pass

def test(console):
    #importlib.reload(module=)
    #use external files
    pass


if __name__ == "__main__":
    THandler = TaskHandler()

    #THandler.disable_log()

    THandler.append_program("Main", main)
    THandler.append_program("TEST", test)
    THandler.set_start_program_func("Main")

    THandler.create_web_site()
    THandler.start_web_site()

    #Autostart the selected programm
    #THandler.create_sys()
    #THandler.start_sys()

    while True:
        try:
            THandler.update()
        except KeyboardInterrupt:
            Debug.okblue("CTRL + C ... Halting")
            THandler.stop_web_site()
            THandler.stop_sys()
            break
    exit(42)
