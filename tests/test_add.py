import pytest

from mvp import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (10, 25, 35),
        (-1, -2, -3),
        (-5, 10, 5),
        (0, 0, 0),
        (0, 123, 123),
        (2**60, 2**60, 2**61),
        (-(2**60), 2**60, 0),
    ],
)
def test_add_parametrized(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("1", 2),
        (1, "2"),
        (None, 2),
    ],
)
def test_add_rejects_obviously_invalid_inputs(a: object, b: object) -> None:
    with pytest.raises(TypeError):
        add(a, b)  # type: ignore[arg-type]


@pytest.mark.xfail(reason="Enable once add() enforces int-only input validation.")
def test_add_rejects_float_inputs_future_validation() -> None:
    with pytest.raises(TypeError):
        add(1.5, 2)  # type: ignore[arg-type]
