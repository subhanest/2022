import pandas as pd

jsondata = pd.read_json(r'words_dictionary.json', orient='index')
jsondata.head()

jsondata.to_csv('englishwords.csv')

csvdata = pd.read_csv(r'englishwords.csv')

df = pd.DataFrame(csvdata)
df2 = df.iloc[:,0]
data_size = df2.size

def load_words():
    with open(r'words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

english_words = load_words()

word = input("Enter word to search: ") 
word = word.lower()

if (word in english_words):
    for i in range(0,data_size):
        if (df2.iloc[i] == word):
            j = i;
            print("Word "+ word+ " is present at " +str(j)+ " index of the dictionary")
else:
    print("Word " + word + " is not present in the dictionary")

