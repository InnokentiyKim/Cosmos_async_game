import asyncio
import random
import curses
import time
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
    curses.curs_set(False)
    canvas.border()
    frames = load_frames(frame_links)
    y, x = curses.window.getmaxyx(canvas)
    coroutines = []
    coroutines.append(animate_spaceship(canvas, frames, y, x))
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
