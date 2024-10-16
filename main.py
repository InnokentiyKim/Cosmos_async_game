import time
import curses
import asyncio
import random


TIC_TIMEOUT = 0.5
symbols = ['+', '*', '.', ':']


async def blink(canvas, row, column, symbol='*', start_delay=0.0):
    while True:
        start_delay = random.randint(0, 2)
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

def draw(canvas):
    canvas.border()
    y, x = curses.window.getmaxyx(canvas)
    stars_amount = 50
    coroutines = []
    for i in range(stars_amount):
        row = random.randint(2, abs(y-3))
        column = random.randint(2, abs(x-3))
        coroutines.append(blink(canvas, row, column, random.choice(symbols)))
    while True:
        try:
            for coro in coroutines:
                coro.send(None)
            canvas.refresh() 
            time.sleep(TIC_TIMEOUT)
        except StopIteration:
            break
    
    
if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
    curses.curs_set(False)
    