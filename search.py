#!/usr/bin/python
import re
import nltk
import sys
import getopt
from nltk.tokenize import *
from collections import deque

#takes in 2 op, return true is op1 has higher or equal precedence than op2
def has_higher_precedence(op_1, op_2):

    if op_2 == '(' or op_2 == ')':
        return False
    if op_1 == 'NOT' and (op_2 == 'AND' or op_2 == 'OR'):
        return True
    if op_1 == 'AND' and op_2 == 'OR':
        return True
    if op_1 == op_2:
        return True

    return False
    

def shunting_yard(query_line):

    #tokenize query
    tokenize_query_list = word_tokenize(query_line)

    #initialise operator stack, takes in boolean operators
    op_stack = []
    #initialise output queue, takes in words
    output_queue = deque()
    #initialise operator list, d/o include brackets
    operator_lst = ['AND', 'OR', 'NOT']
    #initialise bracket list
    bracket_lst = ['(', ')']

    for i in range(len(tokenize_query_list)):
        #get ith token
        token = tokenize_query_list[i]

        #if token is '('
        if token == '(':
            op_stack.append(token)

        #if token is a word 
        if token not in operator_lst and token not in bracket_lst:
            output_queue.append(token)

        #if token is an operator
        if token in operator_lst:

            while( len(op_stack) != 0 and has_higher_precedence(token, op_stack[-1]) ):
                op = op_stack.pop()
                output_queue.append(op)


            op_stack.append(token)

        #if token is ')'
        if token == ')':

            while( len(op_stack) !=0 and op_stack[-1] != '(' ):
                op = op_stack.pop()
                output_queue.append(op)
            
            op_stack.pop()

    while ( len(op_stack) != 0 ):
        op = op_stack.pop()
        output_queue.append(op)
    return output_queue



            


        








def usage():
    print("usage: " + sys.argv[0] + " -d dictionary-file -p postings-file -q file-of-queries -o output-file-of-results")

dictionary_file = postings_file = file_of_queries = output_file_of_results = None
	
try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:p:q:o:')
except getopt.GetoptError as err:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-d':
        dictionary_file  = a
    elif o == '-p':
        postings_file = a
    elif o == '-q':
        file_of_queries = a
    elif o == '-o':
        file_of_output = a
    else:
        assert False, "unhandled option"


if dictionary_file == None or postings_file == None or file_of_queries == None or file_of_output == None :
    usage()
    sys.exit(2)
