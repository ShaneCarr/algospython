def fibit(n):
    if n == 0:
        return 0

    i: int = 0
    sm1: int = 0
    sm2: int = 1

    while i < n:
        t1 = sm1 + sm2   # 0:  0+1 = 1   # 1: T1 = 2    # 2+ 1
        sm1 = sm2        # 0: 1          # 1: 1         #
        sm2 = t1         # 1             # 2            #   3+
        i = i + 1
    return sm1
