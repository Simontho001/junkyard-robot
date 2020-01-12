from dataclasses import dataclass

import cv2
import numpy as np

from opsi.manager.manager_schema import Function
from opsi.util.cv import Mat
from opsi.util.cv.shape import Circles, Segments


class DrawCircles(Function):
    force_enabled = True

    @dataclass
    class Inputs:
        circles: Circles
        img: Mat

    @dataclass
    class Outputs:
        img: Mat

    def run(self, inputs):
        # If there are no circles return the input image
        if inputs.circles is None:
            return self.Outputs(img=inputs.img)

        draw = np.copy(inputs.img.mat.img)

        int_circles = np.uint16(np.around(inputs.circles))

        for pt in int_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(draw, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(draw, (a, b), 1, (0, 0, 255), 3)

        draw = Mat(draw)
        return self.Outputs(img=draw)


class DrawSegments(Function):
    force_enabled = True

    @dataclass
    class Inputs:
        lines: Segments
        img: Mat

    @dataclass
    class Outputs:
        img: Mat

    def run(self, inputs):
        # If there are no circles return the input image
        if inputs.lines is None:
            return self.Outputs(img=inputs.img)

        draw = np.copy(inputs.img.mat.img)

        for line in inputs.lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(draw, (x1, y1), (x2, y2), (255, 0, 0), 3)

        draw = Mat(draw)
        return self.Outputs(img=draw)