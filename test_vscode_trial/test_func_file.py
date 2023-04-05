from VScode_trial import func_file

def test_add():
    assert func_file.add(2, 3) == 5
    assert func_file.add(0, 0) == 0
    assert func_file.add(-1, 1) == 0
    assert func_file.add(100, 2) != 0

def test_sub():
    assert func_file.sub(2, 3) == -1
    assert func_file.sub(0, 0) == 0
    assert func_file.sub(-1, 1) == -2
