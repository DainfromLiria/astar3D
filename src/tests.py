"""
    Unit tests for app.
"""
import subprocess
import pytest

from utils.support import manh_dist, euklid_dist, is_wall, is_in_range, get_random_pos


def test_codestyle():
    """Test codestyle by PEP8.
        R0902: Too many instance attributes (10/7) (too-many-instance-attributes)
        R0801: Similar lines in 2 files
        E1101: Module 'pygame' has no 'QUIT' member (no-member)
    """
    command = "pylint ./**/*.py --disable=R0902,R0801,E1101"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True, check=False)
    result_list = result.stdout.split('\n')[1:-5]
    assert len(result_list) == 0, "Project has PEP8 errors."


@pytest.mark.parametrize(
    'start, end, dist',
    [
        ((10, 9, 8), (12, 11, 10), 6),
        ((-5, -3, 2), (5, 2, -2), 19),
        ((1, 0, 0), (0, 1, -1), 3),
        ((0, 0, 0), (0, 0, 0), 0)

    ])
def test_manh_dist(start, end, dist):
    """Tests for function manh_dist."""
    assert manh_dist(start, end) == dist


@pytest.mark.parametrize(
    'start, end, dist',
    [
        ((10, 9, 8), (12, 11, 10), 3.464),
        ((-5, -3, 2), (5, 2, -2), 11.874),
        ((1, 0, 0), (0, 1, -1), 1.732),
        ((0, 0, 0), (0, 0, 0), 0)

    ])
def test_euklid_dist(start, end, dist):
    """Tests for function euklid_dist."""
    assert euklid_dist(start, end) == dist


@pytest.mark.parametrize(
    'x, y, z, res',
    [
        (0, 12, 10, True),
        (19, 10, 11, True),
        (1, 14, 4, True),
        (0, 0, 0, True),
        (-1, -2, 3, False),
        (2, 3, 4, False)

    ])
def test_is_wall(x, y, z, res):
    """Tests for function is_wall."""
    assert is_wall(x, y, z) is res


@pytest.mark.parametrize(
    'pos, res',
    [
        ((0, 12, 10), False),
        ((19, 10, 11), False),
        ((1, 14, 4), False),
        ((0, 0, 0), False),
        ((-1, -2, 3), False),
        ((2, 3, 4), True),
        ((18, 13, 28), True)
    ])
def test_is_in_range(pos, res):
    """Tests for function is_in_range."""
    assert is_in_range(pos) is res


def test_get_random_pos():
    """Tests for function get_random_pos.
    We assumed, that function is_in_range is correct,
    because we test it in previous tests."""
    for _ in range(10):
        assert is_in_range(get_random_pos()) is True
