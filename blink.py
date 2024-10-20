import asyncio
import random
import curses
import time

from curses_tools import read_controls
from spaceship import animate_spaceship, load_frames


async def blink(canvas, row, column, symbol='*', start_delay=0.0):
    while True:
        start_delay = random.randint(0, 3)
        for i in range(start_delay):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)
        await asyncio.sleep(0)

# def draw_star(canvas, star='*'):
#     while True:
#         canvas.addstr(5, 10, star, curses.A_DIM)
#         canvas.refresh()
#         time.sleep(2)
#         canvas.addstr(5, 10, star)
#         canvas.refresh()
#         time.sleep(0.3)
#         canvas.addstr(5, 10, star, curses.A_BOLD)
#         canvas.refresh()
#         time.sleep(0.5)
#         canvas.addstr(5, 10, star)
#         canvas.refresh()
#         time.sleep(0.3)

TIC_TIMEOUT = 0.1
symbols = ['+', '*', '.', ':']
frame_links = ("src/rocket_frame_1.txt", "src/rocket_frame_2.txt")


def draw(canvas, stars_amount=50):
    frames = load_frames(frame_links)
    y, x = curses.window.getmaxyx(canvas)
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    coroutines = []
    for i in range(stars_amount):
        row = random.randint(2, y-3)
        column = random.randint(2, x-3)
        coroutines.append(blink(canvas, row, column, random.choice(symbols)))
    y_start, x_start = y // 2, x // 2
    space_ship_coro = animate_spaceship(canvas, frames, y_start, x_start)
    while True:
        dy, dx, space = read_controls(canvas)
        if dy or dx:
            x_start, y_start = x_start + dx, y_start + dy
            if space_ship_coro in coroutines:
                coroutines.remove(space_ship_coro)
            space_ship_coro = animate_spaceship(canvas, frames, y_start, x_start)
        coroutines.append(space_ship_coro)
        for coro in coroutines.copy():
            try:
                coro.send(None)
            except StopIteration:
                coroutines.remove(coro)
                break
        time.sleep(TIC_TIMEOUT)
        canvas.refresh()
