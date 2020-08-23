import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()

#Original Test
def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

#Original Test
def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH

def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST

#Original Test
def test_illegal_move_south(robot):
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move_west(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move_east(robot):
    robot.turn()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()

    with pytest.raises(IllegalMoveException):
        robot.move()

#Original Test
def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2

def test_move_north_edge_case(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    state = robot.state()
    assert state['row'] == 1
    assert state['col'] == 1

#Original Test
def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_move(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_once_after_multiple_moves(robot):
    robot.turn()
    robot.move()
    robot.move()
    robot.turn()
    robot.turn()
    robot.turn()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 3

def test_back_track_multiple_after_multiple_moves(robot):
    robot.turn()
    robot.move()
    robot.move()
    robot.turn()
    robot.turn()
    robot.turn()
    robot.move()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1
