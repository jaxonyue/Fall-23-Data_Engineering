from main import add

if __name__ == "__main__":
    test_main()


def test_main():
    assert add(3, 5) == 8
    assert add(1, 2) == 3
    assert add(3, 7) == 10
