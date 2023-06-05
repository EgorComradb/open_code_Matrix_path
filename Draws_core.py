from tkinter import *

class Draws_core:
    frames: {str: object} = {}
    lables: {int: object} = {}
    entery = []
    pp = []

    """Окно в котором все происходит"""
    def window_main(self, root):
        self.frames.clear()
        self.lables.clear()
        self.entery.clear()
        self.pp.clear()

        root.title("window")
        root.geometry(str(1200) + 'x' + str(720))

        main_frame = Frame(root, bg='light blue')
        main_frame.place(relwidth=1, relheight=1)
        self.frames['main_frame'] = main_frame

        params_frame = self.frame_maker(main_frame, color_bg="#83BED7", width=200)
        params_frame.pack(side=RIGHT, fill=Y)
        self.frames["params_frame"] = params_frame

        tile_frame = self.frame_maker(main_frame, color_bg="#A8C2D0", height=700, width=800)
        tile_frame.pack(side=TOP, fill=Y, pady=30)
        self.frames['tile_frame'] = tile_frame

        self.label_pattern(params_frame, text='Введите JSON строку \n (убедитесь что конечная считалась от 0)',
                           bg="#83BED7", width=35).pack(anchor=CENTER, ipady=20, pady=10)
        self.entery_pattern(params_frame, width=35).pack(anchor=CENTER, pady=10)

        self.label_pattern(params_frame, text='Введите начальные координаты \n в формате - 0,0 \n (по умолчанию [0,0]) ',
                           bg="#83BED7", width=35).pack(anchor=CENTER, ipady=20, pady=10)
        self.entery_pattern(params_frame, width=35).pack(anchor=CENTER, pady=10)

        self.button = self.button_create(params_frame, text='Старт', command=self.get_entery).pack(anchor=S, pady=20)

    def get_entery(self):
        self.pp.clear()
        for i in self.entery:
            self.pp.append(i.get())

    def exception(self):
        frame = self.frames['tile_frame']
        self.label_pattern(frame, text="ОШИБКА ВВОДА", bg="light blue", width=40, height=30).pack()


    def tile_maker(self, path, frame, elements, end ,start = None):
        size_x = len(elements[0])
        size_y = len(elements)
        ind = 0
        n_ind = 1
        arrow = ""

        for r in range(size_y):
            for c in range(size_x):
                if [c, r] == end:
                     bg = "red"
                elif [c, r] == start:
                    bg = "green"
                    ind += 1
                    n_ind += 1
                elif [r, c] in path[1]:
                    bg = "#83BED7"
                    print(len(path[1]))
                    if n_ind <= len(path[1]) - 1:
                        if path[1][n_ind][0] - path[1][ind][0] == 1:
                            arrow = '🠗'
                        elif path[1][n_ind][1] - path[1][ind][1] == 1:
                            arrow = '🠖'
                        elif path[1][n_ind][0] - path[1][ind][0] == -1:
                            arrow = '🠕'
                        elif path[1][n_ind][1] - path[1][ind][1] == -1:
                            arrow = '🠔'
                        print(path[1][ind], path[1][n_ind])
                        ind += 1
                        n_ind += 1
                else:
                    arrow = ''
                    bg = "#D9D9D9"
                lable = self.label_pattern(frame, text=str(elements[r][c]) + '\n' + arrow, bg=bg, width=10, height=5)
                lable.grid(column=c, row=r, pady=20, padx=20)


    """--------------------------------------Вспомогательные методы--------------------------------------"""

    """Создание фреймов"""
    def frame_maker(self, frame, color_bg="white", height=1, width=1, relief=None):
        frames = Frame(frame, bg=color_bg, height=height, width=width, relief=relief)
        return frames

    """Создание кнопок"""
    def button_create(self,frame, text='butt', width=7, height=3, command=None):
        button = Button(frame, text=text,
                        width=width, height=height, padx=2.4, bd=1, bg='light blue',
                        activebackground="LightSkyBlue3", command=command, relief="ridge")
        return button

    """Создание лэйблов"""
    def label_pattern(self, frame, text="", bg="white", width=7, height=3):
        label = Label(frame, text=text, bg=bg, width=width, height=height)
        return label

    """Создание полей ввода"""
    def entery_pattern(self, frame, width=7):
        enter = Entry(frame, width=width)
        self.entery.append(enter)
        return enter
