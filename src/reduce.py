"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    >>> reduce(lambda x,y: x*y, [2, 3, 4])
    24
    """
    assert len(x) >= 2
    tmp = 0
    if len(x) == 2:
        return f(x[0], x[1])
    if len(x) > 2:
        tmp = f(x[0], x[1])
        for i in range(2, len(x)):
            tmp = f(tmp, x[i])
        return tmp



def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    >>> accumulate(lambda x,y: x*y, [2, 3, 4])
    [2, 6, 24]
    """
    accumulator = [x[0]]

    for i in range(1, len(x)):
        accumulator.append(f(accumulator[i-1], x[i]))

    return accumulator
