import time
import curses


def draw_star(canvas, star='*'):
    while True:
        canvas.addstr(5, 10, star, curses.A_DIM)
        canvas.refresh()
        time.sleep(2)
        canvas.addstr(5, 10, star)
        canvas.refresh()
        time.sleep(0.3)
        canvas.addstr(5, 10, star, curses.A_BOLD)
        canvas.refresh()
        time.sleep(0.5)
        canvas.addstr(5, 10, star)
        canvas.refresh()
        time.sleep(0.3)

def draw(canvas):
    canvas.border()
    draw_star(canvas)
    time.sleep(1.0)    
    
    
if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
    curses.curs_set(False)
    