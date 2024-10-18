import time
import curses
import random
from blink import blink
from fire_animation import fire


TIC_TIMEOUT = 0.1
symbols = ['+', '*', '.', ':']


def draw(canvas, stars_amount=50):
    canvas.border()
    y, x = curses.window.getmaxyx(canvas)
    coroutines = []
    for i in range(stars_amount):
        row = random.randint(2, abs(y-3))
        column = random.randint(2, abs(x-3))
        coroutines.append(blink(canvas, row, column, random.choice(symbols)))
    while True:
        for coro in coroutines.copy():
            try:
                coro.send(None)
            except StopIteration:
                coroutines.remove(coro)
                break
        time.sleep(TIC_TIMEOUT)
        canvas.refresh()
    
    
if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
    curses.curs_set(False)
    