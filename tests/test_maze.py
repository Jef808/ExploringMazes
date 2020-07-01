import pytest

from lib.maze import Maze

with open("tests/input1.txt", "r", encoding="utf-8") as f:
    width, height = f.readline().rstrip('\n').split(' ')
    maze1 = Maze(width, height, f.read().splitlines())


def test_height_width():
    assert maze1.height == 7
    assert maze1.width == 11


def test_grid():
    assert maze1.grid == [
        "...........", ".#########.", "...#...#...", "S#.#.#.#.#T",
        ".#...#...#.", ".#########.", "..........."
    ]


def test_display(capsys):
    print(maze1)
    captured = capsys.readouterr()
    assert captured.out == """. . . . . . . . . . .
. # # # # # # # # # .
. . . # . . . # . . .
S # . # . # . # . # T
. # . . . # . . . # .
. # # # # # # # # # .
. . . . . . . . . . .
"""


def test_pos():
    p1 = (0, 0)
    p2 = (5, 3)
    p3 = (0, 3)
    assert maze1.pos(p1) == '.'
    assert maze1.pos(p2) == '#'
    assert maze1.pos(p3) == 'S'


def test_find_start_exit():
    assert maze1.find_start_exit() == ((0, 3), (10, 3))
