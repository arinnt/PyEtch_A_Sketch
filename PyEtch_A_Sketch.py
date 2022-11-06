from tkinter import *
from tkinter import ttk

import utilities
from utilities import *

global root_x, root_y, root_w, root_h

root = Tk()
setup_configure_handler(root)

frm = ttk.Frame(root, padding=10, width=root["width"])
# print("root.winfo_width()", root.winfo_width())

#To Do List:
# implement geometry in the  configuration module
# geometry(str(xxx) x str(yyy)
frm.grid()

hex_color_palette = []
for _ in range(1, 10):
    hex_color_palette.append(get_hex_from_rgb_tuple(get_random_rgb_tuple()))

# print(frm.configure().keys())
sketch = Canvas(frm, bg=hex_color_palette[1])

sketch.pack(side='top', fill=BOTH, expand=True)
ttk.Label(frm, text="Hello World!").pack
ttk.Button(frm, text="Quit", command=root.destroy).pack(side='bottom')

btn = ttk.Button(frm)

# control_frame = Frame(frm, )
# print("The options for frame: ", control_frame.configure().keys())
# print("The options for Canvas: ", sketch.configure().keys())
# print("+++++++++++++++++++++++++++++++")
ttk.Button(frm, )

# print(btn.configure().keys())
# print(set(btn.configure().keys()) - set(frm.configure().keys()))

# print(dir(btn))
# print(set(dir(btn)) - set(dir(frm)))

# frm.update()
# root.update()
# frm.config(width=root.winfo_width())
# print("root.winfo_width() =", root.winfo_width())
# print('root.keys() =', root.keys())
#
# print_widget_keys(root.children.items())

# sketch.config(width=root.winfo_width())

root.mainloop()
