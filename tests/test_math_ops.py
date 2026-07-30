"""Tests for the public math helpers."""

import pytest

from mvp import add


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        pytest.param(1, 2, 3, id="positive-integers"),
        pytest.param(-5, -7, -12, id="negative-integers"),
        pytest.param(-5, 8, 3, id="mixed-sign-integers"),
        pytest.param(0, 0, 0, id="zero-values"),
        pytest.param(0, 42, 42, id="zero-left-identity"),
        pytest.param(10**18, 10**18, 2 * 10**18, id="large-integers"),
    ],
)
def test_add_returns_sum_for_integer_inputs(left: int, right: int, expected: int) -> None:
    assert add(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right"),
    [
        pytest.param("1", 2, id="string-left"),
        pytest.param(1, object(), id="object-right"),
        pytest.param(None, 1, id="none-left"),
    ],
)
def test_add_rejects_inputs_that_cannot_be_added(left: object, right: object) -> None:
    """Document error behavior for non-addable inputs until explicit validation exists."""
    with pytest.raises(TypeError):
        add(left, right)  # type: ignore[arg-type]
