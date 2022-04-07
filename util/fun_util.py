from typing import Iterable, Callable


class ExceptionNotFounded:
    pass


def find(predicate: Callable[[object], bool], iterable: Iterable[object]) -> object | None:
    for item in iterable:
        if predicate(item):
            return item
    #return ExceptionNotFounded
    return None