def fibit(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    i: int = 0
    sm1: int = 0
    sm2: int = 1

    while i < n:
        new_sm2 = sm1 + sm2
        sm1 = sm2
        sm2 = new_sm2
        i = i + 1
    return sm1

