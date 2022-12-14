import turtle
from tkinter import *
from tkinter import ttk

import mouseinfo

from utilities import *

global root_x, root_y, root_w, root_h
global window_details
color_etch_a_sketch_body = '#b22023'

hex_color_palette = create_hex_color_palette()


def left():
    etch_screen.onkeypress(None, 'Left')
    etcher.seth(180)
    etcher.forward(5)
    etch_screen.onkeypress(left, 'Left')
    x, y = pos
    print("x, y =", x, y)
    if abs(max(x, y)) > 10:
        print("BOUNCE!!!")


def right():
    etch_screen.onkeypress(None, 'Right')
    etcher.seth(360)
    etcher.forward(5)
    etch_screen.onkeypress(right, 'Right')
    x, y = pos
    if abs(max(x, y)) > 10:
        print("BOUNCE!!!")


def up():
    etch_screen.onkeypress(None, 'Up')
    print(vertical_control_up.state())
    etcher.seth(90)
    etcher.forward(5)
    etch_screen.onkeypress(up, 'Up')


def down():
    etch_screen.onkeypress(None, 'Down')
    etcher.seth(270)
    etcher.forward(5)
    etch_screen.onkeypress(down, 'Down')


def left_button_pressed():
    etcher.seth(180)
    etcher.fd(etcher.width())


def right_button_pressed():
    etch_screen.onkeypress(None, 'Right')
    etcher.seth(360)
    etcher.fd(etcher.width())
    etch_screen.onkeypress(right, 'Right')


def up_button_pressed(kwargs):
    etcher.seth(90)
    etcher.fd(etcher.width())


def down_button_pressed():
    etcher.seth(270)
    etcher.fd(etcher.width())


root = Tk()
setup_configure_handler(root)
root.geometry(str(int(root.winfo_screenwidth() * .9)) + "x" + str(int(root.winfo_screenheight() * .75)))
root.config(bg=color_etch_a_sketch_body)
frm = ttk.Frame(root)
s = ttk.Style()

s.configure('new.TFrame', background=color_etch_a_sketch_body)
print("root.keys()=", )
s.configure('frm.TFrame', background=color_etch_a_sketch_body)
s.configure('controller.TFrame', background=color_etch_a_sketch_body)
s.configure('controller.wide.TButton', background=color_etch_a_sketch_body)
s.configure('controller.tall.TButton', background=color_etch_a_sketch_body)
s.configure("TLabel", background=get_lighter_hex_color(color_etch_a_sketch_body))
s.configure('new.TLabel', background=get_lighter_hex_color(color_etch_a_sketch_body))

# print(s)
# frm = Frame(root)
# print("root.winfo_width()", root.winfo_width())

# To Do List:
# implement geometry in the  configuration module
# geometry(str(xxx) x str(yyy)
frm.grid()

# Creating our red_arrow-image objects
red_arrow_left = PhotoImage(file='red_arrow_left.png')
red_arrow_right = PhotoImage(file='red_arrow_right.png')
red_arrow_up = PhotoImage(file='red_arrow_up.png')
red_arrow_down = PhotoImage(file='red_arrow_down.png')

# Resizing images to fit on button
# subsampling by screensize / 100
red_arrow_image_left = red_arrow_left.subsample(int(root.winfo_screenwidth() / 100),
                                                int(root.winfo_screenheight() / 100))
red_arrow_image_right = red_arrow_right.subsample(int(root.winfo_screenwidth() / 100),
                                                  int(root.winfo_screenheight() / 100))

red_arrow_image_up = red_arrow_up.subsample(int(root.winfo_screenwidth() / 100), int(root.winfo_screenheight() / 100))
red_arrow_image_down = red_arrow_down.subsample(int(root.winfo_screenwidth() / 100),
                                                int(root.winfo_screenheight() / 100))

sketch_canvas = Canvas(frm, bg=hex_color_palette[1])
etcher = turtle.RawTurtle(sketch_canvas)
etch_screen = etcher.getscreen()
etch_screen.onclick(etcher.goto)
# etch_screen.onclick(fxn(etcher, sketch_canvas.winfo_pointerx(), sketch_canvas.winfo_pointery()))

# sketch_canvas.pack(side='top', fill=BOTH, expand=True)
sketch_canvas.pack(side='top')
# sketch_canvas.master.update()
sketch_xpadding = .05 * (frm.master.winfo_width())
sketch_ypadding = .025 * (frm.master.winfo_height())

sketch_canvas.pack(padx=sketch_xpadding, pady=sketch_ypadding)
# ttk.Label(frm, text="Hello World!").pack
# btn = ttk.Button(frm)

controller_frame = ttk.Frame(frm, )
controller_frame.pack(side='bottom')
# ttk.Button(controller_frame, text="Quit", command=root.destroy).grid(column=5, row=3, padx=root.winfo_screenwidth(
# )*.25, sticky='s')

horizontal_control_left = ttk.Button(controller_frame, image=red_arrow_image_left, style='controller.tall.TButton',
                                     command=left_button_pressed)
horizontal_control_left.grid(column=0, row=1, rowspan=2, ipady=root.winfo_screenheight() * .01)
horizontal_control_right = ttk.Button(controller_frame, image=red_arrow_image_right, style='controller.tall.TButton',
                                      command=right_button_pressed)
# horizontal_control_right.grid(column=1, row=1, rowspan=2, sticky='nsew')
horizontal_control_right.grid(column=1, row=1, rowspan=2, ipady=root.winfo_screenheight() * .01)

vertical_control_up = ttk.Button(controller_frame, image=red_arrow_image_up, style='controller.wide.TButton',
                                 command=up)
vertical_control_up.grid(column=9, row=1, ipadx=root.winfo_screenwidth() * .01)
print('vertical_control_up.keys()= ', vertical_control_up.keys())
vertical_control_down = ttk.Button(controller_frame, image=red_arrow_image_down, style='controller.wide.TButton',
                                   command=down_button_pressed)
vertical_control_down.grid(column=9, row=2, ipadx=root.winfo_screenwidth() * .01)

py_etch_label_frame = ttk.Label(controller_frame, text='YAPEtch \'a Sketch')
py_etch_label_frame.grid(column=5, row=2)
quit_button_xpadding = (root.winfo_screenwidth() * .6) / 2
ttk.Button(controller_frame, text="Quit", command=root.destroy).grid(column=5, row=4, padx=quit_button_xpadding,
                                                                     sticky='s')

# for i in range(controller_frame.winfo_width()+1):
#     controller_frame.grid_columnconfigure(i, weight=1, uniform="foo")

print(controller_frame.children)
for k, v in controller_frame.children.items():
    print(k, v)

# root.update()
print("frm.master.winfo_height()=", frm.master.winfo_height())
# frm.config(height=frm.master.winfo_height(), bg=color_etch_a_sketch_body)
frm.config(height=frm.master.winfo_height(), width=frm.master.winfo_width())
sketch_canvas.config(width=frm.master.winfo_width() - (2 * sketch_xpadding),
                     height=.75 * frm.master.winfo_height())
# controller_frame.config(height=.9 * controller_frame.master.winfo_height(),
# width=controller_frame.master.winfo_width(), bg=color_etch_a_sketch_body)
controller_frame.config(height=controller_frame.master.winfo_height() - sketch_canvas.winfo_height(),
                        width=controller_frame.master.winfo_width(), style="controller.TFrame")
# py_etch_label_frame.config(width=int(.05 * py_etch_label_frame.master.winfo_width()),
#                            height=int(.05 * py_etch_label_frame.master.winfo_height()))
py_etch_label_frame.config(background=color_etch_a_sketch_body, style="TFrame")
frm.config(style="frm.TFrame")
# etcher.setpos(sketch_canvas.winfo_width()/2, sketch_canvas.winfo_height()/2)
# etcher.setpos(0,0)

horizontal_control_left.config(width=int(horizontal_control_left.master["width"]))
print(int(horizontal_control_left.master["width"]))
print(horizontal_control_left.master.winfo_width())
# print('globals()=', globals())
# if window_details in globals():
#     if window_details is not window_details:
#         sketch_canvas.config(width=root.winfo_width() - 4, height=root.winfo_height() - 80)

# root.bind("space", up_button_pressed)
# root.bind('space', up_button_pressed)
root.bind('<space>', up_button_pressed)


def a_pressed(x):
    print(x)
    # etcher.fd(etcher.width())
    left_button_pressed()


def d_pressed(x):
    print(x)
    # etcher.fd(etcher.width())
    right_button_pressed()


def s_pressed(x):
    print(x)
    # etcher.fd(etcher.width())
    down_button_pressed()


def w_pressed(x):
    print(x)
    # etcher.fd(etcher.width())
    up_button_pressed(x)


root.bind('w', w_pressed)
root.bind('a', a_pressed)
root.bind('s', s_pressed)
root.bind('d', d_pressed)
etch_screen.onkeypress(left, 'Left')
etch_screen.onkeypress(right, 'Right')
etch_screen.onkeypress(up, 'Up')
etch_screen.onkeypress(down, 'Down')

pos = etcher.pos()
print(etcher.xcor())
etch_screen.listen()

root.mainloop()
