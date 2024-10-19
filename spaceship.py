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


async def animate_spaceship(canvas, frames, max_rows, max_columns):
    """Draw animation of spaceship on canvas."""

    frames = cycle(frames)
    row = max_rows // 2
    column = max_columns // 2

    for frame in frames:
        draw_frame(canvas, row, column, frame)
        await asyncio.sleep(0)
    await asyncio.sleep(0)

