from sample import adder, sample


def test_fib() -> None:
    assert sample.fib(0) == 0
    assert sample.fib(1) == 1
    assert sample.fib(2) == 1
    assert sample.fib(3) == 2
    assert sample.fib(4) == 3
    assert sample.fib(5) == 5
    assert sample.fib(10) == 55


def test_adder() -> None:
    assert adder.add_one(0) == 1
    assert adder.add_one(1) == 2
