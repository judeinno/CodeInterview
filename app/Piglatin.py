class PigLatinConverter(object):

    def __init__(self, args):
        self.args = args

    def pig_latin(self):
        """ This converter converts an english statement into pig latin
        """
        pig = 'way'
        pyg = 'ay'
        vowels = "aeiouAEIOU"
        save_initial_word = self.args + '\n'
        data = open('data.txt', 'a')
        data.write(save_initial_word)
        data.close()
        if len(self.args) > 0 and self.args.isalpha():
            word = self.args.lower()
            first = word[0]
            for i in vowels:
                if first == i:
                    new_word = word + pig
                    print(new_word)
                    save_new_word = new_word + '\n'
                    data = open('data.txt', 'a')
                    data.write(save_new_word)
                    data.close()
                    return new_word
                    break
                else:
                    vowel_index = 0
                    for letter in word:
                        if letter not in vowels:
                            vowel_index += 1
                            continue
                        else:
                            break
                    new_word = word[vowel_index:] + word[:vowel_index] + "ay"
                    print(new_word)
                    save_new_word = new_word + '\n'
                    data = open('data.txt', 'a')
                    data.write(save_new_word)
                    data.close()
                    return new_word
                    break

        else:
            print('Please enter a word')
            return ('Please enter a word')


if __name__ == '__main__':
    word_input = input('Enter a word: ')
    args = PigLatinConverter(word_input)
    PigLatinConverter.pig_latin(args)