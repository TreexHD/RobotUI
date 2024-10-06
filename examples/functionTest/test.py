from robotui.debug import Debug
from robotui.main import TaskHandler

import time

def prog1(console):
    i = 0
    while True:
        console("[BLUE]" + str(i) + "[END]")
        i += 1
        time.sleep(1)

def prog2(console):
    i = 100
    while True:
        console("[GREEN]" + str(i) + "[END]")
        i -= 1
        time.sleep(1)


if __name__ == "__main__":
    THandler = TaskHandler()

    THandler.set_update_rate(1)
    #THandler.disable_log()

    THandler.append_program("Prog1", prog1)
    THandler.append_program("Prog2", prog2)
    THandler.set_start_program_func("Prog1")

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