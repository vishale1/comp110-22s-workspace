"""Demonstrate defining a module imported elswhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to power of n."""
    return x ** n


if __name__ == "__main__":
    main()
else:
    print(f"helper.py was imported: {__name__}")