import time
import curses
import asyncio


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
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
    coroutines = [blink(canvas, 2, i+2) for i in range(5)]
    while True:
        try:
            for coro in coroutines:
                coro.send(None)
            canvas.refresh() 
            time.sleep(1)
        except StopIteration:
            break
    
    
if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
    curses.curs_set(False)
    