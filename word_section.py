import os

alpha = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'


def wrr(tab, sign, length):
    with open("./podzielone/" + sign + "/" + length + ".txt", 'w') as f:
        for i in range(len(tab)):
            f.write(tab[i])


def mkdir():
    for sign in alpha:
        try:
            os.makedirs("./podzielone/" + sign)
        except:
            pass


def save_sign(SignedTab):
    tab = []
    sign = SignedTab[0][0]

    for i in range(8):
        tab.append([])

    i = 0
    while i < len(SignedTab):
        if 10 > len(SignedTab[i]):
            if 2 < len(SignedTab[i]):
                tab[len(SignedTab[i]) - 3].append(SignedTab[i])
        else:
            tab[7].append(SignedTab[i])
        i += 1

    for i in range(7):
        if tab[i]:
            wrr(tab[i], sign, str(i + 2))

    wrr(tab[7], sign, 'more')


def do_tab_of_signs(full_tab):
    tab = []
    j = 0
    i = 0
    sign = alpha[j]
    tab.append([])
    while i < len(full_tab):
        if sign == full_tab[i][0]:
            tab[j].append(full_tab[i])
            i += 1
        else:
            tab.append([])
            j += 1
            if j >= len(alpha):
                break
            sign = alpha[j]
    return tab


def read(name):
    f = open(name)
    tab = list(f)

    return tab


def do():
    mkdir()
    full_tab = read("slowa.txt")
    tab = do_tab_of_signs(full_tab)

    for i in tab:
        if i:
            save_sign(i)

    print("finito")


if __name__ == "__main__":
    do()
