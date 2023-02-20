from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_hy():
    assert value("hy") == 20
    assert value("Hy") == 20

def test_other():
    assert value("welcome") == 100
    assert value("230") == 100
    assert value(",._") == 100
