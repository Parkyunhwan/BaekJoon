# https://www.acmicpc.net/source/13468575
import sys

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())


def get_squared_diff(x1, x2):
    return (x2 - x1) ** 2


start, end = 0, 100  # (relative time, 0~100%)
answer = sys.maxsize
while end - start > 10 ** -6:
    left = start + (end - start) * (1 / 3)
    right = start + (end - start) * (2 / 3)

    dist_x_at_left_1 = Ax + (Bx - Ax) * (left / 100)
    dist_x_at_left_2 = Cx + (Dx - Cx) * (left / 100)
    dist_y_at_left_1 = Ay + (By - Ay) * (left / 100)
    dist_y_at_left_2 = Cy + (Dy - Cy) * (left / 100)

    dist_x_at_left = get_squared_diff(dist_x_at_left_1, dist_x_at_left_2) + get_squared_diff(dist_y_at_left_1,
                                                                                             dist_y_at_left_2)

    dist_x_at_right_1 = Ax + (Bx - Ax) * (right / 100)
    dist_x_at_right_2 = Cx + (Dx - Cx) * (right / 100)
    dist_y_at_right_1 = Ay + (By - Ay) * (right / 100)
    dist_y_at_right_2 = Cy + (Dy - Cy) * (right / 100)

    dist_x_at_right = get_squared_diff(dist_x_at_right_1, dist_x_at_right_2) + get_squared_diff(dist_y_at_right_1,
                                                                                                dist_y_at_right_2)

    if dist_x_at_left <= dist_x_at_right:
        answer = min(answer, dist_x_at_left)
        end = right
    else:
        answer = min(answer, dist_x_at_right)
        start = left

print("%.10f" % (answer ** 0.5))