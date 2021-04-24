class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def print_information(self):
        print(f'"{self.title}" '
              f'by {self.artist} '
              f'({self.year}) '
              f'hangs in the {self.museum}.')


def main():
    Painting(
        input(),
        input(),
        input(),
    ).print_information()


if __name__ == '__main__':
    main()
