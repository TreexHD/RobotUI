from robotui.debug import Debug
from robotui.main import TaskHandler
import time


def main():
    i = 1
    while True:
        print(i)
        time.sleep(3)
        i += 1


if __name__ == "__main__":
    THandler = TaskHandler()

    THandler.disable_log()
    THandler.set_start_program_func(main)

    THandler.create_web_site()
    THandler.start_web_site()

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
