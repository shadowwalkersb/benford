from collections import Counter
from math import log
from pathlib import Path
from matplotlib.figure import Figure


def benfords_law(c):
    return log(1. + 1. / c) / log(10)


def lead_digit(num):
    """
    >>> lead_digit('2.134')
    '2'
    >>> lead_digit('5.134e-5')
    '5'
    >>> lead_digit('0.134')
    '1'
    >>> lead_digit('0.0034')
    '3'
    """
    num = "%e" % float(num)

    return num[0]


def save_plot(title, x, y1, y2, to_file):
    fig = Figure()
    ax = fig.subplots()

    ax.set_title(title)
    ax.set_xlabel('k')
    ax.set_ylabel('P(k)')


    ax.plot(x, y1, 'x', label="Result")
    ax.plot(x, y2, label="Bernard's Law")

    ax.legend(loc="upper right")

    fig.savefig(to_file)


def get_lead_digits_from_file(fname, col, num_headers=0):
    if not Path(fname).is_file():
        return zip(*[(d, 0, benfords_law(d)) for d in range(1, 10)])

    counter = Counter()
    
    with open(fname) as fin:
        for _ in range(num_headers):
            fin.readline()  # Skip headers

        for line in fin.readlines():
            pop = line.split()[col]
            counter[int(lead_digit(pop))] += 1

    tot = sum(counter.values())
    data = sorted([(c, counter[c] / tot, benfords_law(c)) for c in counter])
    digits, data_prob, benfords_prob = zip(*data)

    return digits, data_prob, benfords_prob


def process_file_and_save_plot(from_file, col, title, to_file):
    digits, data_prob, benfords_prob = get_lead_digits_from_file(from_file, col, num_headers=1)

    save_plot(title=title,
              x=digits,
              y1=data_prob,
              y2=benfords_prob,
              to_file=to_file)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
