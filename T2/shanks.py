import utils


def shanks_algorithm(alpha=6, beta=248388, p=458009):
    m = int(p ** .5) + 1
    y1 = alpha**m % p
    y2 = utils.inv_mod(alpha, p)
    frst_list, scnd_list = [], []

    for i in range(m):
        frst_list.append([i, y1**i % p])
        scnd_list.append([i, beta * (y2**i) % p])

    for i in frst_list:
        for j in scnd_list:
            if i[1] == j[1]:
                return m*i[0] + j[0]
