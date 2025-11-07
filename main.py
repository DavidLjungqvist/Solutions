import time

def current_milli_time():
    return round(time.time() * 1000)


def main():
    toggle_time = 10000
    is_on = True
    while True:
        time = current_milli_time()
        if toggle(time, toggle_time, is_on):
            is_on = not is_on
        print(time)
        print(is_on)



def toggle(current_time, toggle_time, condition):
    truncated_time = current_time // 10
    truncated_toggle = toggle_time // 10
    if truncated_time % truncated_toggle == 0 and not condition:
        return True
    elif (truncated_time + toggle_time) % truncated_toggle == 0 and condition:
        return True
    else:
        return False

main()
