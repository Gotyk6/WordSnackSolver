import itertools
import operator

from fileManager import FilesManger


class Solver:
    def __init__(self, alphabeth="abcdefghijklmnopqrstuvwxyz", dictionaries_folder_name="div"):
        self.alphabeth = alphabeth
        self.folder_name = dictionaries_folder_name
        self.fm = FilesManger(self.folder_name, self.alphabeth)

    @staticmethod
    def prepare_list_of_permutations(signs, length):
        sequence = [''.join(p) for p in itertools.permutations(signs, length)]
        return list(map(operator.itemgetter(0), itertools.groupby(sorted(sequence))))

    def get_correct_words(self, letters, length):
        permutation_tab = self.prepare_list_of_permutations(letters, length)

        global literals_tab
        word_list = []
        for char in self.alphabeth:
            if char in letters:
                literals_tab = self.fm.read_dictionary(char, length)
                if literals_tab:
                    for word in permutation_tab:
                        if word in literals_tab:
                            word_list.append(word)

        return word_list


if __name__ == "__main__":
    solver = Solver()
    while True:
        letters = input("Give me letters (ex. abba): ")
        length = int(input("Give me word length: "))
        print("Answers: ", "\n".join(solver.get_correct_words(letters, length)))
