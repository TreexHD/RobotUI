from robotui.debug import Debug
from robotui.main import TaskHandler
#from yourprog import your_progr1, your_progr2


def main(console):
    #use extra files!!! like this...
    #your_progr1(console)
    pass # remove this

def test(console):
    #your_progr2(console)
    pass # remove this


if __name__ == "__main__":
    THandler = TaskHandler()

    THandler.set_update_rate(1)
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