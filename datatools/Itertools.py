

def window(iterable, n):
    """takes an iterable and a number and returns a sliding buffer"""
    window = []
    for i, e in enumerate(iterable):
        window.append(e)
        if i >= n:
            window.pop(0)
            yield window
        if i == n - 1:
            yield window
