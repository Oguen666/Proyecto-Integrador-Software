def make_chocolate(small, big, goal):
    max_big = goal // 5
    if max_big > big:
        max_big = big

    remaining = goal - (max_big * 5)

    if remaining <= small:
        return remaining
    else:
        return -1
