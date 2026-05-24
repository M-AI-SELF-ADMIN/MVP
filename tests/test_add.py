import pytest

from mvp import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (123, 456, 579),
        (-1, -2, -3),
        (-10, 5, -5),
        (0, 0, 0),
        (0, 42, 42),
        (2**60, 2**60, 2**61),
        (10**18, -10**18, 0),
    ],
)
def test_add_parametrized(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("1", 2),
        (1.5, 2),
        (None, 1),
    ],
)
@pytest.mark.xfail(
    reason="Input validation is not implemented yet; enable when add() enforces int inputs.",
    strict=False,
)
def test_add_rejects_invalid_inputs_future_validation(a: object, b: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        add(a, b)  # type: ignore[arg-type]
