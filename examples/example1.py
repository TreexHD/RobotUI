from robotui.debug import Debug
from robotui.main import TaskHandler
import time


def main(console):
    i = 1
    while True:
        console("[RED]"+ str(i) + "[END]")
        time.sleep(.5)
        i += 1

def test(console):
    i = 100
    while True:
        console("[GREEN]"+ str(i) + "[END]")
        time.sleep(.5)
        i -= 1


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
