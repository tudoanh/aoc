import re
import numpy as np
import math
from collections import Counter, defaultdict, namedtuple, deque
from itertools import (
    permutations,
    combinations,
    chain,
    cycle,
    product,
    islice,
    takewhile,
    zip_longest,
    count as count_from,
)
from functools import lru_cache, total_ordering
from dataclasses import dataclass


def Input(day, line_parser=str.strip, file_template="inputs/input_{}.txt"):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))


def integers(text):
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r"-?\d+", text))


def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


letters = "abcdefghijklmnopqrstuvwxyz"
cat = "".join


def first(iterable, default=None):
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def nth(iterable, n):
    return next(islice(iter(iterable), n, n + 1))


def quantify(iterable, pred=bool):
    "Count how many items in iterable have pred(item) true."
    return sum(map(pred, iterable))


def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def first_true(iterable, pred=None, default=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true."""
    # first_true([a,b,c], default=x) --> a or b or c or x
    # first_true([a,b], fn, x) --> a if fn(a) else b if fn(b) else x
    return next(filter(pred, iterable), default)


def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield c


def length(iterable):
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)


def shuffled(iterable):
    "Create a new list out of iterable, and shuffle it."
    new = list(iterable)
    random.shuffle(new)
    return new


def compose(f, g):
    "The function that computes f(g(x))."
    return lambda x: f(g(x))


def multiply(numbers):
    "Multiply all the numbers together."
    result = 1
    for n in numbers:
        result *= n
    return result


origin = (0, 0)


def distance(P, Q=origin):
    "Straight-line (hypotenuse) distance between two points."
    return sum((p - q) ** 2 for p, q in zip(P, Q)) ** 0.5


def cityblock_distance(P, Q=origin):
    "Manhatten distance between two points."
    return sum(abs(p - q) for p, q in zip(P, Q))


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return overlapping(iterable, 2)
