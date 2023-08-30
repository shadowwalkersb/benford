import filecmp

from ..benford import *


def test_get_lead_digits_from_file1():
    x, y1, y2 = get_lead_digits_from_file('tests/one_column_no_header.txt', col=0)

    assert x == (3, 5, 6, 7, 8, 9)
    assert y1 == (0.4, 0.1, 0.1, 0.2, 0.1, 0.1)

def test_get_lead_digits_from_file2():
    x, y1, y2 = get_lead_digits_from_file('tests/one_column_one_line_header.txt', col=0, num_headers=1)

    assert x == (3, 5, 6, 7, 8, 9)
    assert y1 == (0.4, 0.1, 0.1, 0.2, 0.1, 0.1)

def test_get_lead_digits_from_file3():
    x, y1, y2 = get_lead_digits_from_file('tests/one_column_two_lines_header.txt', col=0, num_headers=2)

    assert x == (3, 5, 6, 7, 8, 9)
    assert y1 == (0.4, 0.1, 0.1, 0.2, 0.1, 0.1)

def test_save_plot():
    save_plot("Test1",
              [1,2,3],
              [0.5, 0.7, 0.65],
              [0.52, 0.68, 0.652],
              'tests/benford_test.png')

    # filecmp.clear_cache()
    # print("FILE CMP", filecmp.cmp('tests/benford_test.png', 'tests/benford_test.png'))
    assert filecmp.cmp('tests/benford_test.png', 'tests/benford_ref.png')
