"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jessica Myers.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    corner1x = rectangle.corner_1.x
    corner1y = rectangle.corner_1.y
    corner2x = rectangle.corner_2.x
    corner2y = rectangle.corner_2.y
    width = rectangle.get_width()
    height = rectangle.get_height()

    corner1x = corner1x - (width * .5 * (n - 1))
    corner2x = corner2x - (width * .5 * (n - 1))
    corner1y = corner1y - (height * (n - 1))
    corner2y = corner2y - (height * (n - 1))

    original_corner1x = corner1x
    original_corner2x = corner2x

    for k in range(n):
        for j in range(n - k):
            newRectangle = rg.Rectangle(rg.Point(corner1x + (.5 * width * k), corner1y),
                                        rg.Point(corner2x + (.5 * width * k), corner2y))
            newRectangle.attach_to(window)
            window.render(.1)

            corner1x = corner1x + width
            corner2x = corner2x + width
        corner1y = corner1y + height
        corner2y = corner2y + height
        corner1x = original_corner1x
        corner2x = original_corner2x


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
