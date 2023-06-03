from json import JSONDecodeError
from tkinter import *
import Draws_core
import matrix_create
import matrix_analize
import threading
import time


class Start:
    draw = Draws_core.Draws_core()
    check = matrix_create.matrix_create()
    root = Tk()
    # JSON_string = '{"board":[[0,10,4],[2,6,7],[1,2,3],[2,6,7],[5,6,3],[8,4,5],[7,9,1],[3,6,5]], "target":[2,2]}'

    def __init__(self):
        self.draw.window_main(self.root)
        self.start_calculations = False
        self.thread = threading.Event()
        threading.Thread(target=self.passed).start()

        self.root.mainloop()
        self.thread.set()

    def passed(self):
        try:
            while not self.start_calculations:
                if self.thread.is_set(): return
                if len(self.draw.pp) != 2:
                    continue
                self.start_calculations = True

            if self.check.check(json_string=self.draw.pp[0]):
                matrix = matrix_create.matrix_create.matrix[0]
                end = matrix_create.matrix_create.end[0]
                start = [0, 0] if self.draw.pp[1] == '' else [int(self.draw.pp[1][0]), int(self.draw.pp[1][2])]

                if matrix_analize.matrix_analize(end_coordinate=end, elements=matrix, start_coordinate=start):
                    path = matrix_analize.matrix_analize.result[0]
                    tile_frame = self.draw.frames['tile_frame']
                    params_frame = self.draw.frames['params_frame']

                    self.draw.tile_maker(frame=tile_frame, path=path, elements=matrix, end=end, start=start)
                    self.draw.label_pattern(params_frame, text="сумма весов " + path[0], bg="#A8C2D0", width=20, height=5).pack()

                    clear_button = self.draw.button_create(frame=params_frame, text="Очистить",command=self.restart)
                    clear_button.pack(pady=5)

        except (TypeError, IndexError, AttributeError, RuntimeError, ValueError, JSONDecodeError):
            self.draw.exception()
            time.sleep(3)
            self.restart()

    def restart(self):
        self.thread.set()
        Start()

if __name__ == '__main__':
    Start()
