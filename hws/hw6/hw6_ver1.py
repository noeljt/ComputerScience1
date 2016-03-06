"""
A program to compare villains.

Author: Joe Noel (noelj)
"""

import textwrap
#Villain, firstyear, lastyear, doc.no, docactor, episodes, totalstories,
#motivation, story titles

def read_file(file1):
    #makes list of villains from file
    villains = []
    for line in open(file1):
        villains.append(line.split('	'))
    del villains[0]
    return villains

def stories(villains):
    #returns list of tuples with villain name and involved stories
    stories = []
    for villain in villains:
        #This is a hard-coded exception as the format was wrong in the .tsv file
        #The stories were seperated by only commas instead of comma + space
        if villain[0] == 'Master (the)':
            stories.append( (villain[0],\
                             villain[8].replace('\n','').split(',')) )
        else:
            stories.append( (villain[0],\
                             villain[8].replace('\n','').split(', ')) )
    return stories

def v_stories(stories, villain):
    #returns list of villains appearing at same time and list of unique
    #appearances
    for villains in stories:
        if villains[0] == villain:
            v_stories = villains[1]
            break
    same_story = []
    for v_story in v_stories:
        for s_list in stories:
            for story in s_list[1]:
                if v_story == story:
                    if s_list[0] != villain:
                        same_story.append(s_list[0])
    same_story = list(set(same_story))
    same_story.sort()
    o_stories = []
    for villains in same_story:
        for villains2 in stories:
            if villains == villains2[0]:
                o_stories += villains2[1]
    o_stories = set(o_stories)
    unique_stories = list(set(v_stories) - o_stories)
    unique_stories.sort()
    allies = ''
    for villains in same_story:
        if villains == same_story[0]:
            allies += villains
        else:
            allies += ', ' + villains
    just_villain = ''
    for story in unique_stories:
        if story == unique_stories[0]:
            just_villain += story
        else:
            just_villain += ', ' + story
    return (allies, just_villain)
                
    
    
def top_ten(villains):
    #prints top 10 villains based on appearances and returns list
    popularity = []
    for villain in villains:
        popularity.append( (int(villain[6]),villain[0]) )
    popularity.sort(reverse=True)
    top_ten = popularity[0:10]
    print ''
    for n in range(10):
        print "%d. %s" %((n+1),popularity[n][1])    
    return top_ten

def pick_villain(top_ten, villains, stories):
    #asks for user input and prints info of villain
    print "Please enter a number between 1 and 10, or -1 to end"
    villain = raw_input('Enter a villain ==> ')
    print villain
    if villain == '-1':
        print "Exiting"
    elif villain.isdigit() == True and int(villain) > 0 and int(villain) <= 10:
        print "%s in %s stories, with the following other villains:" \
          %(top_ten[int(villain)-1][1],top_ten[int(villain)-1][0])
        allies,just_villain = v_stories(stories, top_ten[int(villain)-1][1])
        print '=' * 50
        for line in textwrap.wrap(allies,68):
            print '\t' + str(line)
        print ''
        if len(just_villain) == 0:
            print "There are no stories with only this villain"
            print '=' * 50
            print ''
            for n in range(10):
                print "%d. %s" %((n+1),top_ten[n][1])
            pick_villain(top_ten,villains, stories)
        else:
            print "The stories that only features %s are:" \
                  %(top_ten[int(villain)-1][1])
            print '=' * 50
            for line in textwrap.wrap(just_villain,68):
                print '\t' + str(line)
            print '\n'
            for n in range(10):
                print "%d. %s" %((n+1),top_ten[n][1])
            pick_villain(top_ten,villains, stories)        
        
    else:
        print ''
        for n in range(10):
            print "%d. %s" %((n+1),top_ten[n][1])
        pick_villain(top_ten,villains, stories)

if __name__ == '__main__':
    file1 = 'DrWhoVillains.tsv'
    villains = read_file(file1)
    top_ten = top_ten(villains)
    stories = stories(villains)
    pick_villain(top_ten,villains,stories)