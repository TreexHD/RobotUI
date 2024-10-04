from robotui.debug import Debug
from robotui.main import TaskHandler
import time


def main():
    print("Hello")
    time.sleep(1)


if __name__ == "__main__":
    THandler = TaskHandler()

    THandler.create_web_site()
    THandler.start_web_site()

    THandler.create_sys(main)
    THandler.start_sys()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            Debug.okblue("CTRL + C ... Halting")
            THandler.stop_web_site()
            THandler.stop_sys()
            break
    exit(42)
