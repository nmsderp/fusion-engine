from fusionengine.engine.debug import DEBUGIMAGE
import fusionengine.backend.gl as gl

import pygame as pg
from pygame.locals import DOUBLEBUF, OPENGL


class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        """
        Creates a a base window for your game. This is the main window you will use for your application.

        Args:
            title (str): The title of your window
            width (int): The width of your window
            height (int): The height of your window
        """

        pg.init()

        self._running = False
        self._fps = 60
        self._quittable = True
        self._clock = pg.time.Clock()

        self.title = title
        self.width = width
        self.height = height

        try:
            self.window = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
            pg.display.set_caption(title)

            program_icon = pg.image.load(DEBUGIMAGE)
            pg.display.set_icon(program_icon)

            self._running = True

        except Exception:
            print("Error: Can't create a window.")

        try:
            gl.Ortho(0, width, height, 0, -1, 1)

            gl.Enable(gl.BLEND)
            gl.Enable(gl.TEXTURE_2D)

            gl.BlendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)

        except Exception:
            print("Error: Can't setup OpenGL.")

    def change_icon(self, image_path: str) -> None:
        """
        Changes icon of the window.

        Args:
            Icon_Path (str): Path to your icon

        """

        programIcon = pg.image.load(image_path)
        pg.display.set_icon(programIcon)

    def loop(self, your_loop) -> None:
        """
        A while loop decorator function. The main way to start a main loop.

        Args:
            your_loop (function): Your main loop function
        """
        while self.running():
            your_loop()

    def running(self) -> bool:
        """
        Returns if the window is running. Used for the main loop.

        Returns:
            bool: returns true if the window is running else false
        """
        self._refresh()
        return self._running

    def set_fps(self, fps: int) -> None:
        """
        Sets the desired frames per second for the game loop.

        Args:
            fps (int): The desired frames per second
        """
        self._fps = fps

    def get_fps(self) -> int:
        """
        Returns the current desired frames per second for the game

        Returns:
            int: The current desired FPS
        """

        return self._fps

    def quit(self) -> None:
        """
        Quits the window. Specifically, stops and deletes window.
        """
        self._running = False

    def toggle_quittable(self) -> None:
        """
        Toggles whether the window is quittable.
        """
        self._quittable = not self._quittable

    def _refresh(self) -> None:
        """
        Does all things for refreshing window. (Do not use!)
        """

        self.DELTATIME = self._clock.tick(self._fps)

        for event in pg.event.get():
            if event.type == pg.QUIT and self._quittable:
                self.quit()

        pg.display.flip()
        pg.time.wait(10)

        gl.Clear(gl.DEPTH_BUFFER_BIT)
        gl.Clear(gl.COLOR_BUFFER_BIT)
