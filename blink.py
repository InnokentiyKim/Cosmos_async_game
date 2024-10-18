import asyncio
import random
import curses


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