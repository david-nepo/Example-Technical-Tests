"""Tests for main functions."""


from main import (
    count_letters,
    get_score,
    get_points_for_word,
    get_alphabet
)


def test_count_letters():

    assert count_letters('ABB') == [('A', 1), ('B', 2)]


def test_get_score_basic():

    assert get_score([('A', 1), ('B', 2)]) == 7


def test_get_points_for_word():

    assert get_points_for_word('ABB') == 7


def test_get_alphabet():

    assert get_alphabet() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
