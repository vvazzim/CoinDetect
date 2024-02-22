import numpy as np

def see_lines(height, width, lines):
    image = np.zeros((height, width))

    for line in lines:
        i-start, j-start, i-end, j-end, j-end= line

    def plot_line(x0, y0, x1, y1):
        dx, dy = x1 - x0, y1 - y0
        if dx == 0:
            image[min(y0, y1):max(y0, y1) + 1, x0] = 1
        else:
            error = 0
            delta_error = abs(dy / dx)
            y = y0
            for x in range(x0, x1 + 1):
                image[y, x] = 1
                error += delta_error
                while error >= 0.5 and (y1 > y0 or y1 < y0):
                    image[y, x] = 1
                    y += np.sign(y1 - y0)
                    error -= 1

    for line in lines:
        plot_line(*line)

    return image