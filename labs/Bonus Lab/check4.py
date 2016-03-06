"""
Too late to write a description.

Author: Joe Noel (noelj)
"""

from collections import OrderedDict
from operator import itemgetter

def graph_file(file1):
    d = {}
    for line in open(file1):
        l = line.strip().split()
        s1 = set()
        for i in l[1:]:
            s1.add(int(i))
        d[int(l[0])] = s1
    return d

def name_file(file1):
    d = {}
    for line in open(file1):
        l = line.strip().split('|')
        d[int(l[1])] = l[0]
    return d

def score(d):
    scores = {}
    for node in d.keys():
        scores[node] = 1/float(len(d))
    return scores

def get_newscores(current_scores, graph):
    new_scores = {}
    N = len(graph)
    for key in current_scores: 
        new_scores[key]= 0.15/N
    for p in graph:
        M = len(graph[p])
        for q in graph[p]:
            new_scores[q] += 0.85 * current_scores[p]/M
    return new_scores

if __name__ == '__main__':
    file1 = raw_input('Edge File ==> ')
    graph = graph_file(file1)
    file2 = raw_input('Name File ==> ')
    names = name_file(file2)
    initial_scores = score(graph)
    current_scores = get_newscores(initial_scores, graph)
    
    print "%d people total" %(len(graph))

    threshold = 0.00001
    diff = 0
    for p in graph.keys():
        diff += abs(initial_scores[p]-current_scores[p])

    while diff > threshold:
        initial_scores = current_scores
        current_scores = get_newscores(current_scores, graph)
        temp_diff = 0
        for p in graph.keys():
            temp_diff += abs(initial_scores[p]-current_scores[p])
        diff = temp_diff
    
    d = OrderedDict(sorted(current_scores.items(), key=itemgetter(1), reverse=True))   
    
    
    k = int(raw_input('Number (k) ==> '))
    i = 1
    for item in d.keys()[0:k]:
        print "%d. %s" %((i), names[item])
        i += 1
    
    
