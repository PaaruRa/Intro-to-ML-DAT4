import numpy as np
import rotations


def main():
    points = np.array([[2, 1], 
                       [3, 2], 
                       [0, 3]])

    rotated_points = rotations.rotate(points, direction='anti-clockwise')

    print(rotated_points)


if __name__ == '__main__':
    main()
