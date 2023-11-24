"""Main script."""

import string

# Getting points for each word


def count_letters(input: str) -> list[tuple]:
    """Get letter count."""

    unique_letters = set(input)

    output = []
    for letter in unique_letters:
        count = input.count(letter)
        output.append((letter, count))

    return sorted(output)


def get_score(letter_points: list[tuple]) -> int:

    points_dict = {
        1: ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }

    count = 0
    for letter in letter_points:
        for key, value in points_dict.items():
            if letter[0] in value:
                count += (key * letter[1])

    return count


def get_points_for_word(input: str) -> int:
    """Get actual points for word."""

    letter_points = count_letters(input)

    points = get_score(letter_points)

    return points


def get_alphabet() -> str:
    """Gets alphabet in capitals."""

    return string.ascii_uppercase

# def get_random


if __name__ == "__main__":
    get_score([('A', 1), ('B', 2)])
