import itertools
import operator
import os


class FilesManger:
    def __init__(self, folder_name, file_names):
        self.directory_path = "dictionary.txt"
        self.dictionaries_folder_name = folder_name
        if not os.path.exists("./" + folder_name):
            self.create_dictionaries(file_names)

    def create_dictionaries(self, names):
        self.create_directories(names)
        with open(self.directory_path) as f:
            main_dictionary = list(f)
            words = self.create_list_of_words(main_dictionary, names)

            for i in words:
                if i:
                    self.save_sign(i)

    def create_directories(self, names):
        for name in names:
            try:
                os.makedirs("./" + self.dictionaries_folder_name + "/" + name)
            except FileExistsError as ex:
                print(ex)

    def create_list_of_words(self, full_tab, names):
        tab = []
        for char in names:
            innerTab = []
            for i in range(len(full_tab)):
                if char == full_tab[i][0]:
                    innerTab.append(full_tab[i])
                else:
                    tab.append(innerTab)
                    full_tab=full_tab[i:]
                    break
        return tab

    def read_word_list(self, name, length):
        tab = None
        try:
            with open("./" + self.dictionaries_folder_name + "/" + name + "/" + str(length) + ".txt") as f:
                tab = f.read().splitlines()
        except FileNotFoundError as ex:
            print(ex)

        return tab

    def save_sign(self, SignedTab):
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
                self.save(tab[i], sign, str(i + 2))

        self.save(tab[7], sign, 'more')

    def save(self, tab, sign, length):
        with open("./div/" + sign + "/" + length + ".txt", 'w') as f:
            for i in range(len(tab)):
                f.write(tab[i])


class Solver:
    def __init__(self):
        self.alphabeth = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
        FilesManger("div", self.alphabeth)
        pass

    def prepare_list_of_permutations(self, signs, len):
        sequence = [''.join(p) for p in itertools.permutations(signs, len)]
        return list(map(operator.itemgetter(0), itertools.groupby(sorted(sequence))))

    def create_dictionaries(self):
        pass

    def read(self, sign, length):
        tab = None
        try:
            with open("./div/" + sign + "/" + str(length) + ".txt") as f:
                tab = f.read().splitlines()
        except FileNotFoundError:
            pass

        return tab

    def equalizer(self, word, length):
        word_list = []
        permutation_tab = self.prepare_list_of_permutations(word, length)
        j = 0
        sign = permutation_tab[0][0]
        literals_tab = self.read(sign, length)

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
                    if j >= len(self.alphabeth) - 1:
                        return word_list
                    if self.alphabeth[j] in word:
                        sign = self.alphabeth[j]
                        literals_tab = self.read(sign, length)
                        break

        return word_list


if __name__ == "__main__":
    solver = Solver()
    print("\n".join(solver.equalizer('btuaosu', 4)))
