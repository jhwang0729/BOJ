import sys

from math import floor

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireballs: list[list[int]] = [list(map(int, input().split())) for _ in range(M)]
# grid: list[list[int]] = [[]]
di: list[int] = [-1, -1, 0, 1, 1, 1, 0, -1]
dj: list[int] = [0, 1, 1, 1, 0, -1, -1, -1]


def move(fireballs: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    for fireball in fireballs:
        r, c, m, s, d = fireball
        new_r, new_c = (r + s * di[d]) % N, (c + s * dj[d]) % N
        out.append([new_r, new_c, m, s, d])
    return out


def update(fireballs: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    aux = {}  # [(i, j)] = [idx]
    for idx in range(len(fireballs)):
        i, j, _, _, _ = fireballs[idx]
        if (i, j) in aux:
            aux[(i, j)].append(idx)
        else:
            aux[(i, j)] = []
            aux[(i, j)].append(idx)

    for fireball_idx in aux.keys():
        # fireball_idx = tuple[i, j]
        i, j = fireball_idx

        if len(aux[fireball_idx]) > 1:
            num_fireballs: int = len(aux[fireball_idx])
            combined_m: int = 0
            combined_s: int = 0
            ds = []

            fireball_indicies = aux[fireball_idx]
            for fireball_index in fireball_indicies:
                _, _, m, s, d = fireballs[fireball_index]
                combined_m += m
                combined_s += s
                ds.append(d)

            if floor(combined_m / 5) <= 0:
                continue
            else:
                all_odd: bool = all(elem % 2 == 1 for elem in ds)
                all_even: bool = all(elem % 2 == 0 for elem in ds)
                positive: list[int] = [0, 2, 4, 6]
                negative: list[int] = [1, 3, 5, 7]

                for cnt in range(4):
                    out.append([i, j, floor(combined_m / 5), floor(combined_s / num_fireballs),
                                positive[cnt] if all_odd or all_even else negative[cnt]])

        else:
            out.append(fireballs[aux[fireball_idx][0]])

    return out


def solve(fireballs: list[list[int]]) -> int:
    for _ in range(K):
        # print(f'about to pass fireballs to move {fireballs}')
        fireballs = move(fireballs)
        # print(f'middle {fireballs}')
        fireballs = update(fireballs)
        # print(f'after {fireballs}')


    out: int = 0
    for fireball in fireballs:
        out += fireball[2]

    return out


ans: int = solve(fireballs)

print(ans)
