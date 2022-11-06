import random
import time
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
