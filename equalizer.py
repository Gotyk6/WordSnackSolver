from word_section import alpha
from permutations import perm


def read(sign, length):
    tab = None
    try:
        with open("./div/" + sign + "/" + str(length) + ".txt") as f:
            tab = f.read().splitlines()
            # f = open("./div/" + sign + "/" + str(length) + ".txt")
            # tab = list(f)
    except:
        pass

    return tab


def equalizer(word, length):
    word_list = []
    permutation_tab = perm(word, length)
    j = 0
    sign = permutation_tab[0][0]
    literals_tab = read(sign, length)

    w = 0
    while w < len(permutation_tab):
        if sign == permutation_tab[w][0]:
            if literals_tab:
                if permutation_tab[w] in literals_tab:
                    word_list.append(permutation_tab[w])
            w += 1
        else:

            while True:
                j += 1
                if j >= len(alpha) - 1:
                    return word_list
                if alpha[j] in word:
                    sign = alpha[j]
                    literals_tab = read(sign, length)
                    break

    return word_list


print("\n".join(equalizer('btuaosu', 4)))
