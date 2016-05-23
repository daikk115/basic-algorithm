import sys


def remove_special_characters(word):
    word = word.replace(',','').replace('!','').replace('-','').replace('_','').replace('.','').replace('?','')
    word = word.lower()
    return word

def convert_to_list(dict_words):
    list_words = []
    for key in dict_words:
        list_words.append([dict_words[key][0], key, dict_words[key][1]])
    return list_words

output = {}
words = []
with open(sys.argv[1]) as f:
    i = 1
    for line in f:
        line = line.replace('\n',' ')
        line = line.replace('\t',' ')
        list_words = line.split()
        for word in list_words:
            word = remove_special_characters(word)
            if word in words:
                output[word][0] += 1
                if i not in output[word][1]:
                    output[word][1].append(i)
            else:
                words.append(word)
                output[word] = []
                output[word].append(1)
                output[word].append([i])

        i = i + 1

    output = convert_to_list(output)

output = sorted(output, key=lambda word: (word[0], word[1]), reverse=True)
for word in output:
    print word