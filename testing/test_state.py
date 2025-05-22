from unittest import mock
import pytest
from app.domain.state import toggle_mode, tick_timer, reset_timer


def test_toggle_rest():
    assert toggle_mode("Rest") == "Work"


def test_toggle_focus():
    assert toggle_mode("Work") == "Rest"


# Simple testing
def test_toggle_invalid():
    with pytest.raises(ValueError, match="Invalid mode"):
        toggle_mode("nap")


# For looping
@pytest.mark.parametrize(("input", "expected"), [(0, 1), (1, 2)])
def test_tick_timer(input, expected):
    assert tick_timer(input) == expected
    assert tick_timer(input) == expected


# Catching a function and mocking it
@mock.patch("testing.test_state.toggle_mode", return_value="apple")
def test_toggle_mock(mock2):
    assert toggle_mode("Rest") == "apple"


@mock.patch("testing.test_state.tick_timer", return_value=18)
def test_prompt(mockl):
    assert tick_timer(1) == 18


def test_reset():
    assert reset_timer() == 0
