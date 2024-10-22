import asyncio
from curses_tools import draw_frame, get_frame_size, read_controls
from itertools import cycle


def load_frames(links):
    """Load animation frames from files."""
    frames = []
    for link in links:
        with open(link) as file:
            frame = file.read()
            frames.append(frame)
    return frames


async def animate_spaceship(canvas, frames, start_row, start_column):
    """Draw animation of spaceship on canvas."""

    frames = cycle(frames)
    row = start_row
    column = start_column

    for frame in frames:
        draw_frame(canvas, row, column, frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, frame, negative=True)
        

def spaceship_move(x, y, dx, dy):
    return x + dx, y + dy


