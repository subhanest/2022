import pandas as pd

jsondata = pd.read_json(r'C:\Users\DELL\Desktop\NCRA Task 1\english-words-master\words_dictionary.json', orient='index')
jsondata.head()

jsondata.to_csv('englishwords.csv')

csvdata = pd.read_csv(r'englishwords.csv')
csvdata.tail()