import sys
import warnings
from collections import deque

import pytest

from lib.agent import Agent
from lib.maze import Maze

with open("tests/input1.txt", "r", encoding="utf-8") as f:
    width, height = f.readline().rstrip('\n').split(' ')
    maze1 = Maze(width, height, f.read().splitlines())

agent = Agent(maze1)

with open("tests/input2.txt", "r", encoding="utf-8") as f:
    width, height = f.readline().rstrip('\n').split(' ')
    maze2 = Maze(width, height, f.read().splitlines())

agent2 = Agent(maze2)

print(agent2.maze, file=sys.stderr)


def test_init():
    assert agent.maze == maze1
    assert agent.start == (0, 3)


def test_valid_square():
    pos1 = (1, 1)
    pos2 = (-1, 0)
    pos3 = (0, -1)
    pos4 = (0, 7)
    pos5 = (11, 0)
    pos6 = (0, 0)
    pos7 = (10, 3)
    assert agent.valid_square(pos1) == False
    assert agent.valid_square(pos2) == False
    assert agent.valid_square(pos3) == False
    assert agent.valid_square(pos4) == False
    assert agent.valid_square(pos5) == False
    assert agent.valid_square(pos6) == True
    assert agent.valid_square(pos7) == True


def test_move():
    pos = (1, 2)
    mov = (0, -1)
    assert agent.move(pos, mov) == (1, 1)


def test_possible_moves():
    pos1 = (0, 3)
    pos2 = (4, 2)
    pos3 = (10, 2)
    assert agent.possible_next(pos1) == {(0, 4), (0, 2)}
    assert agent.possible_next(pos2) == {(5, 2), (4, 3)}
    assert agent.possible_next(pos3) == {(9, 2), (10, 3), (10, 1)}


def test_final_state():
    pos1 = (10, 3)
    pos2 = (10, 4)
    pos3 = (3, 1)
    assert agent.final_state(pos1) == True
    assert agent.final_state(pos2) == False
    assert agent2.final_state(pos3) == True


def test_find_shortest_path():
    assert agent2.find_shortest_path() is None
    assert isinstance(agent.find_shortest_path(), deque)


def test_solve_maze():
    assert agent2.shortest_path_length() == "DOOMED"
    assert agent.shortest_path_length() == 16
