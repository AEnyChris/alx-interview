#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    '''Implements and returns the winner of the prime game'''
    scores = {
            'Maria': 0,
            'Ben': 0
        }

    for n in nums[:x]:
        seq = [i for i in range(1, n+1)]
        player = 'Maria'
        p = 2
        if len(seq) > 1:
            while len(seq) > 1:
                if p in seq:
                    if p * p <= n:
                        for i in range(p * p, n + 1, p):
                            if i in seq:
                                seq.pop(seq.index(i))
                    seq.pop(seq.index(p))
                    if len(seq) > 1:
                        player = 'Ben' if player == 'Maria' else 'Maria'
                p += 1
        else:
            player = 'Ben'
        scores[player] += 1
    if scores.get('Ben') == scores.get('Maria'):
        return None
    if scores.get('Ben') > scores.get('Maria'):
        res = 'Ben'
    else:
        res = 'Maria'
    return res


if __name__ == '__main__':
    x = 6
    nums = [2, 5, 1, 4, 3, 30]
    print(isWinner(x, nums))
