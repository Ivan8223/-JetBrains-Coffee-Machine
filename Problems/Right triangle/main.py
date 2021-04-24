class RightTriangle:

    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = round(self.a * self.b / 2, 1)

    def get_area(self):
        return self.area


def is_triangle_right(c, a, b):
    return c**2 == a**2 + b**2


def main():
    input_c, input_a, input_b = [int(x) for x in input().split()]

    print(is_triangle_right(input_c, input_a, input_b)
          and RightTriangle(input_c, input_a, input_b).get_area()
          or "Not right")


if __name__ == '__main__':
    main()
