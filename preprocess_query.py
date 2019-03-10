import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

set_stopwords = set(stopwords.words('english'))
bool_set = set()
bool_set.add('OR')
bool_set.add('AND')
bool_set.add('NOT')
punc_set = set(string.punctuation)

ps = PorterStemmer()

#input: takes in a query
#output: returns a query, which has punctuations removed, converted to lower case, non-boolean words are stemmed too.
def preprocess_query(query):

    #remove punctuation from query
    query = ''.join(ch for ch in query if ch not in punc_set)
    word_token_list = word_tokenize(query)

    #convert to lowercase and do stemming
    for i in range(len(word_token_list)):
        if word_token_list[i] not in bool_set:
            word_token_list[i] = ps.stem(word_token_list[i].lower())

    return ' '.join(word_token_list)
    
    
    
    

    
    



