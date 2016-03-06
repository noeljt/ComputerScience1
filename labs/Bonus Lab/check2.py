"""
Create initial scores and implement function to change scores.

Author: Joe Noel (noelj)
"""

def read_file(file1):
    d = {}
    for line in open(file1):
        l = line.strip().split()
        s1 = set()
        for i in l[1:]:
            s1.add(int(i))
        d[int(l[0])] = s1
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
    file1 = raw_input('File ==> ')
    graph = read_file(file1)
    initial_scores = score(graph)
    new_scores = get_newscores(initial_scores, graph)
    
    print "%d people total" %(len(graph))
    for key in graph.keys():
        print "%d:" %(key), graph[key]
    
    mystr = ""
    for p in sorted(initial_scores.keys()):
        mystr += "%d: %.4f " %(p, initial_scores[p])
    print "Initial scores\n\t" + mystr
    
    mystr = ""
    for p in sorted(new_scores.keys()):
        mystr += "%d: %.4f " %(p, new_scores[p])
    print "Computed scores\n\t" + mystr