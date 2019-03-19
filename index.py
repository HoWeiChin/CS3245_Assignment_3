#!/usr/bin/python
import re
import nltk
import sys
import getopt
import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import _pickle as cPickle
import math

#for code development
trng_dir = 'C:/Users/Wei Chin/Desktop/CS3245/HW #2/reuters/reuters/training'

set_stopwords = set(stopwords.words('english'))
punc = "()[.,?!'\";:-]/+>$*^`&"
#initialised inverted_index, key == words, value = posting list
inverted_index = {}

doc_weight_map = {}

#preprocess token_list, return a preprocessed dic of words (dic key) and their term freqs (dic value)
def process_token_list(token_list):
    ps = PorterStemmer()
    processed_dic = {}

    for token in token_list:
        #skip numbers
        if any(char.isdigit() for char in token):
            continue
        #skip stop words
        if token in set_stopwords:
            continue
        #skip punctuation tokens
        if token in punc:
            continue
        if token == ' ':
            continue
        else:
            if any(char in punc for char in token):
                token = ''.join(char for char in token if char not in punc)
            if token != ' ':
            #stem a word token 
                processed_token = ps.stem(token)
                if processed_token not in processed_dic:
                    processed_dic[processed_token] = 1
                else:
                    processed_dic[processed_token] += 1
                
    return processed_dic



#preprocess line, return a preprocessed set of words 
def process_line(line):
    #convert everything to lowercase
    line = line.lower()
    #tokenize line
    token_list = word_tokenize(line)
    processed_words_dic = process_token_list(token_list)
    return processed_words_dic
        
#preprocess a reuters_doc, return a set of words perculiar to that document
def process_reuters_file(reuters_doc, docID):

    f = open(reuters_doc, 'r')
    word_dic_for_doc = {}

    for line in f:
        if line != '\n':
        #get dictionary of words, term freq pairs obtained from that line
            words_dic_for_line = process_line(line)
            

        #for word_dic_for_doc, store words as keys and tuple of (docID, term_freq) as value
            for word_key in words_dic_for_line:
                if word_key != '':
                    if word_key not in word_dic_for_doc:
                        term_freq = words_dic_for_line[word_key]
                        tup = (int(docID), term_freq)
                        word_dic_for_doc[word_key] = tup

    return word_dic_for_doc

#populate inverted_index with dic of words, tuple of (docID, tf) for each reuters document
def populate_index(doc_word_dic):

    for word in doc_word_dic:
        tup = doc_word_dic[word]

        if word not in inverted_index:
            inverted_index[word] = [tup]
        else:
            inverted_index[word].append(tup)

def compute_weight(tf):
    tf = 1 + math.log10(tf)
    return tf 

def store_doc_level_weights(term, sorted_list, reuters_file_lst):
    
    appear_lst = []
    for tup in sorted_list:
        docID, weight = tup
        if docID not in doc_weight_map:
            doc_weight_map[docID] = [(term, weight)]
        else:
            doc_weight_map[docID].append((term, weight))
        appear_lst.append(docID)
    
    for doc_i in reuters_file_lst:
        if int(doc_i) not in appear_lst:
            if int(doc_i) not in doc_weight_map:
                doc_weight_map[int(doc_i)] = [(term, 0)]
            else:
                doc_weight_map[int(doc_i)].append((term, 0))


def index(reuters_dir, dic_file, post_file):
    reuters_file_lst = os.listdir(reuters_dir)
    reuters_file_lst = sorted([int(ele) for ele in reuters_file_lst])
   
    count = 5
    for doc in reuters_file_lst:
        if count == 0:
            break
        doc = str(doc)
        #get full path of doc
        doc_full = os.path.join(reuters_dir, doc)
       
        #get set of words from that doc
        doc_word_dic = process_reuters_file(doc_full, doc)
       
        #populate inverted_index with doc_word_dic and that particular docID
        if len(doc_word_dic) > 0:
            populate_index(doc_word_dic)
        count -= 1
    
    #write output file for dictionary and postings
    d_f = open(dic_file, 'w+')
    p_f = open('posting_humanreadable.txt', 'w+')
    p_picke_f = open(post_file, 'wb')

    for term in sorted(inverted_index.keys()):
        #write dictionary keys
        print(term)
        line_df = term + ' ' + str(p_picke_f.tell())  + '\n'
        d_f.write(line_df)

        #write posting values and is human-readable
        lst = inverted_index[term]
        
        df = len(lst)
        #convert to tf-idf
        for i in range(len(lst)):
            tup = lst[i]
            docID, tf = tup
            weight = compute_weight(tf)
            lst[i] = (docID, weight) 
        sorted_lst = sorted(lst, key=lambda element : element[1])
        idf = math.log10(7769/df)
        line_pf = str(idf) + ' '+ str(sorted_lst) + '\n'
        p_f.write(line_pf)
        store_doc_level_weights(term, sorted_lst, reuters_file_lst)
        sorted_lst.append(idf)
        cPickle.dump(sorted_lst, p_picke_f)
    d_f.close()
    p_f.close()
    p_picke_f.close()

    d_f_1 = open('doc.txt', 'w+')
    p_f_1 = open('weight_humanreadable.txt', 'w+')
    p_picke_f_1 = open('weight.txt', 'wb')
    
    for doc in sorted(doc_weight_map.keys()):
        weight_list = doc_weight_map[doc]
        sorted_weight_list = weight_list
        line_df_1 = str(doc) + ' '+ str(p_picke_f_1.tell()) + '\n'
        d_f_1.write(line_df_1)

        line_pf_1 = str(sorted_weight_list) + '\n'
        p_f_1.write(line_pf_1)
        cPickle.dump(sorted_weight_list, p_picke_f_1)
    d_f_1.close()
    p_f_1.close()
    p_picke_f_1.close()




def usage():
    print("usage: " + sys.argv[0] + " -i directory-of-documents -d dictionary-file -p postings-file")


input_directory = output_file_dictionary = output_file_postings = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:d:p:')

except getopt.GetoptError as err:
    usage()
    sys.exit(2)
    
for o, a in opts:
    if o == '-i': # input directory
        input_directory = a
    elif o == '-d': # dictionary file
        output_file_dictionary = a
    elif o == '-p': # postings file
        output_file_postings = a
    else:
        assert False, "unhandled option"

if input_directory == None or output_file_postings == None or output_file_dictionary == None:
    usage()
    sys.exit(2)
index(input_directory, output_file_dictionary, output_file_postings)










