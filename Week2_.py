import math


def euclideanDistance(list):

    x1 = list[0][0]
    x2 = list[1][0]
    y1 = list[0][1]
    y2 = list[1][1]

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    points = [(x1, y1), (x2, y2)]
    print(euclideanDistance(points))


if __name__ == '__main__':
    main()
