"""Example of a funtion that searches through a list."""


def main() -> None:
    print(contains("Kanye West", ["Kanye West", "Pete Davidson"]))


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()