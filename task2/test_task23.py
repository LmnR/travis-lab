import io


def test_input():
    f = io.open('task2/input.txt', mode='r', encoding='utf-8')
    assert len(f.readline().rstrip('\n')) == 6
    f.close()
