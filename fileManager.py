import os


class FilesManger:
    def __init__(self, folder_name, file_names):
        self.dictionary_path = "dictionary.txt"
        self.folder_with_dictionaries = folder_name
        if not os.path.exists("./" + folder_name):
            self.create_dictionaries(file_names)

    def create_dictionaries(self, names):
        self.create_directories(names)
        with open(self.dictionary_path) as f:
            main_dictionary = list(f)
            words = self.slice_list(main_dictionary, names)

            for i in words:
                if i:
                    self.save_words(i)

    def create_directories(self, names):
        for name in names:
            try:
                os.makedirs("./" + self.folder_with_dictionaries + "/" + name)
            except FileExistsError as ex:
                print(ex)

    def slice_list(self, whole_list, characters):
        tab = []
        whole_list = [x for x in whole_list if x.startswith(tuple(characters))]

        for char in characters:
            inner_tab = []
            for i in range(len(whole_list)):
                if char == whole_list[i][0]:
                    inner_tab.append(whole_list[i])
                else:
                    whole_list = whole_list[i:]
                    break
            tab.append(inner_tab)

        return tab

    def save_words(self, table):
        tab = self.divide_by_length(table)
        sign = table[0][0]

        for i in range(len(tab) - 1):
            if tab[i]:
                self.save(tab[i], sign, str(i + 2))

        self.save(tab[7], sign, 'more')

    def divide_by_length(self, words):
        tab = []
        for i in range(8):
            tab.append([])

        for word in words:
            if 10 < len(word):
                tab[-1].append(word)
            elif 2 < len(word):
                tab[len(word) - 3].append(word)
        return tab

    def save(self, tab, sign, length):
        with open("./" + self.folder_with_dictionaries + "/" + sign + "/" + str(length) + ".txt", 'w') as f:
            for i in range(len(tab)):
                f.write(tab[i])

    def read_dictionary(self, sign, length):
        tab = None
        try:
            with open("./" + self.folder_with_dictionaries + "/" + sign + "/" + str(length) + ".txt") as f:
                tab = f.read().splitlines()
        except FileNotFoundError as ex:
            print(ex)

        return tab
