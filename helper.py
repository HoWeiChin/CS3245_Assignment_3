import numpy as np
import math

N = 7769

#accept term freq of a term t and doc freq of a term t
def compute_tf_idf(tf, df):
    idf = math.log10(N/df)
    tf = 1 + math.log10(tf)
    return tf * idf

#accept a query weight vector as a list and a document weight vector as a list
def n_cosine_similarity(q_vec, d_vec):
    #conversion to np_array
    q_np_vec = np.asarray(q_vec, dtype=float)
    d_np_vec = np.asarray(d_vec, dtype=float)
    dot_product = np.dot(q_np_vec, d_np_vec)

    q_sqrt_dist = compute_vec_distance(q_np_vec)
    d_sqrt_dist = compute_vec_distance(d_vec)

    return dot_product / (q_sqrt_dist * d_sqrt_dist)

#accepts a list which is a representation of a vector
def compute_vec_distance(vec):
    sum = 0
    for ele in vec:
        sum += ele ** 2
    return math.sqrt(sum)





