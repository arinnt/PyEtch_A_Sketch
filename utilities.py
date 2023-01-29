import random
import time

from PIL import ImageColor

global window_details


def get_rgb_tuple_from_time():
    time_based_r = (int(time.strftime("%H")) * int(255 / 24)) % 255
    time_based_g = (int(time.strftime("%M")) * int(255 / 60)) % 255
    time_based_b = (int(time.strftime("%S")) * int(255 / 60)) % 255
    print('Time Based R=', time_based_r)
    print('Time Based G=', time_based_g)
    print('Time Based B=', time_based_b)
    rgb = (time_based_r, time_based_g, time_based_b)
    return rgb


def get_random_rgb_tuple():
    random_r = random.randint(0, 255)
    random_g = random.randint(0, 255)
    random_b = random.randint(0, 255)
    random_rgb_tuple = (random_r, random_g, random_b)
    return random_rgb_tuple


def get_hex_from_rgb_tuple(rgb):
    hex_r = hex(rgb[0]).strip('0x')
    # hex_r = hex(rgb[0]).partition('0x')
    # print("hex_r =", hex_r)
    hex_g = hex(rgb[1]).strip('0x')
    hex_b = hex(rgb[2]).strip('0x')
    # hex_digits = [hex_r, hex_g, hex_b]
    # for _ in hex_digits:
    #     while len(_) < 3:
    #         _ = str(0) + str(_)
    while len(hex_r) < 2:
        hex_r = str('0') + hex_r
    while len(hex_g) < 2:
        hex_g = str('0') + hex_g
    while len(hex_b) < 2:
        hex_b = str('0') + hex_b

    # print('hex_r, hex_g, hex_b= ', hex_r, hex_g, hex_b)
    # print("str('#'+hex_r + hex_g + hex_b) = ", str('#' + hex_r + hex_g + hex_b))
    return str('#' + hex_r + hex_g + hex_b)


def get_rgb_from_float(rgb_float):
    r = int(rgb_float[0] * 254)
    g = int(rgb_float[1] * 254)
    b = int(rgb_float[2] * 254)
    return (r, g, b)


def get_random_color_int():
    color_number = random.randint(1, 255)
    # green = random.randint(1, 255)
    # blue = random.randint(1, 255)
    return color_number


def configure_handler(event):
    # print(event)
    results = str.split((str(event).strip('>')), ' ')
    r = {}
    # next we remove items without '='
    for _ in range(0, len(results) - 1):
        if results[_].__contains__('='):
            # print('results[', _, ']=', results[_])
            k, v = str.split(results[_], '=')
            # print('k=', k)
            # print('v=', v)
            # (str.split('='))
            r[k] = v
        else:
            results.remove(results[_])
        # print('r=', r)
        global window_details
        window_details = r
        # print("window_details=", window_details)

    # print("window_details=", window_details)
    # print("results =", results)
    return r


def setup_configure_handler(root_tk):
    root_tk.bind("<Configure>", configure_handler)


def print_widget_keys(widget):
    print('Welcome to widget Wizard!')
    try:
        widget.update()
    except:
        print('Error, but that\'s okay!')
    print('Widget:', str(widget))
    for key in widget.keys():
        print('key:value =', key, ':', widget[key])
        # print('value=', root[key])
        # print('value= ', value)


def get_lighter_hex_color(original_hex_color):
    original_rgb_color = ImageColor.getcolor(original_hex_color, "RGB")
    original_rgb_color = str(original_rgb_color).strip('()')
    # print(original_rgb_color)
    rgb_tuple = original_rgb_color.split(', ')
    # print("rgb_tuple=", rgb_tuple)
    r, g, b = rgb_tuple
    dark_r = (int(r) + 10) % 255
    dark_g = (int(g) + 10) % 255
    dark_b = (int(b) + 10) % 255

    dark_r = hex(dark_r).strip('0x')
    dark_g = hex(dark_g).strip('0x')
    dark_b = hex(dark_b).strip('0x')

    while len(dark_r) < 2:
        dark_r = str('0') + dark_r
    while len(dark_g) < 2:
        dark_g = str('0') + dark_g
    while len(dark_b) < 2:
        dark_b = str('0') + dark_b
    return str('#' + dark_r + dark_g + dark_b)


def fill_widget_children(parent_widget):
    for (string, widget) in parent_widget.children.items():
        # print("string=", string)
        # print("widget=", widget)
        # rgb = (get_random_color_number(), get_random_color_number(), get_random_color_number())
        rgb = get_random_rgb_tuple()
        # widget.config(bg=get_lighter_hex_color(widget.master["background"]))
        fg = widget["background"]
        for i in range(1, 15):
            # lighten our color 15 times
            fg = get_lighter_hex_color(fg)
        try:
            widget.config(fg=fg)
        except:
            print('Widget:', str(widget), "doesn't have a fg variable")
        w = max(widget.master.winfo_reqwidth(), widget.master.winfo_width())
        widget.configure(width=w)

        # widget.config(sticky='nsew')


def create_hex_color_palette():
    hex_color_palette = []
    for _ in range(1, 10):
        hex_color_palette.append(get_hex_from_rgb_tuple(get_random_rgb_tuple()))
    return hex_color_palette


# method to perform action
def fxn(x_turtle, x, y):
    x_turtle.goto(x, y)
    x_turtle.write(str(x) + "," + str(y))
    print("THgagfilusnflaskjnf")


def get_position(i,j):
    print("(", i, "," ,j,")")
    return
