import logging
import argparse

from cachecontrol._cmd import setup_logging


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.logger = logging.Logger('logger')

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.width = new_width
        else:
            raise ValueError

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self.length = new_length
        else:
            raise ValueError

    def __str__(self):
        return f'Прямоугольник: {self.width} X {self.length}'

    def __repr__(self):
        return f"Прямоугольник: ({self.width}, {self.length})"

    def get_area(self) -> float:
        return self.width * self.length

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)


def setup_logging():
    logging.basicConfig(filename='Rectangle.log',filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description="Прямоугольник:")
    parser.add_argument('--width', type=float, help='Ширина')
    parser.add_argument('--length', type=float, help='Длина')
    namespace = parser.parse_args()
    setup_logging()

    try:
        rect_1 = Rectangle(namespace.width, namespace.length)
        print(rect_1)


    except ValueError as e:
        logging.error(f"Ошибка: {e}")


if __name__ == '__main__':
    main()

