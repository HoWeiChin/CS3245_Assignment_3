from math import sqrt

#linked list implementation of skip_list, class node == linked list node
class node:

    def __init__ (self, data, next_node=None, skip_node=None):
        print("initialising node with data of " + str(data))
        self.data = data
        self.next_node = next_node
        self.skip_node = skip_node
        print('complete!')

    #all get methods
    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next_node
    
    def get_skip_node(self):
        return self.skip_node
    
    #all set methods
    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_skip_node(self, skip_node):
        self.skip_node = skip_node

class skip_list:
    head_node = None
    last_node = None
    length = 0
    list_of_nodes = []

    #when you initialise skiplist, the 1st node will be initialised too,
    #must provide constructor with data to create head node
    def __init__ (self, head_node=None, last_node=None):
        self.head_node = head_node
        self.last_node = last_node
    
    #print entire skip list content, for debugging purposes
    def print_skip_list(self):
        curr_node = self.head_node
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next_node
    
    
    def build_skip_list(self, postings_lst):

        skip_interval = int(sqrt(len(postings_lst)))

        #for loop will build posting nodes
        self.list_of_nodes.append( node(postings_lst[0]) )
        for i in range(1, len(postings_lst)):
            curr_node = node( postings_lst[i] )
            prev_node = self.list_of_nodes[i-1]
            prev_node.set_next_node(curr_node)
            self.list_of_nodes.append(curr_node)


        self.length = len(self.list_of_nodes)
        #for loop will create skip pointers
        if skip_interval > 0:
            for i in range(0 , self.length , skip_interval):
                if i == self.length -1:
                    break
                curr_node = self.list_of_nodes[i]
                skip_node = self.list_of_nodes[i + skip_interval]
                curr_node.set_skip_node(skip_node)
        self.head_node = self.list_of_nodes[0]
        self.last_node = self.list_of_nodes[self.length-1]
        



            

    
    
    
