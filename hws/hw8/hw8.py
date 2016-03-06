
import json
from hw8util import *

class Restaurant(object):
    def __init__(self, d):
        self.reviews = d['review_count'] #integer
        self.name = d['name'] #string
        self.address = d['full_address'] #string
        self.latitude = d['latitude'] #float
        self.longitude = d['longitude'] #float
        self.categories = d['categories'] #list of strings
        lower_cat = []
        for cat in d['categories']:
            lower_cat.append(cat.lower())
        self.categories_lower = lower_cat
        self.stars = d['stars'] #float
    
    def __str__(self):
        return "%s (%d reviews, %.1f stars) [%s]" %\
               (self.name, self.reviews, self.stars,\
                self.address.replace('\n',' '))
    
    def dist(self, lat2, lon2):
        return dist(self.latitude, self.longitude,\
                    lat2, lon2)
def search_location():
    loc = raw_input('Where (-1 to exit) ==> ')
    print loc
    loc = loc.lower()
    dictLoc = {}
    if loc == '-1':
        return True
    elif loc == "":
        return True
    else:
        for rest in Rdict:
            if loc in Rdict[rest].address.lower():
                dictLoc[rest] = Rdict[rest]
    
    cat = raw_input('Filter by what ==> ')
    print cat
    cat = cat.lower()
    cats = {}
    listCat = []
    if cat != '':
        if ',' in cat:
            listCats = cat.split(',')
            i = 0
            for cat in listCats:
                temp_cat = cat.strip().lower()
                if temp_cat[0] != '~':
                    listCats[i] = temp_cat
                i += 1
            initial_catlist = []
            for rest in dictLoc:
                if listCats[0] in dictLoc[rest].categories_lower:
                    initial_catlist.append(dictLoc[rest])
            for cat in listCats:
                temp_catlist = []
                for rest in dictLoc:
                    if cat in dictLoc[rest].categories_lower:
                        temp_catlist.append(dictLoc[rest])
                initial_catlist = list(set(initial_catlist) & set(temp_catlist))
            
            
            for rest in initial_catlist:
                for cat in rest.categories:
                    if cat in cats:
                        cats[cat] += 1
                    else:
                        cats[cat] = 1
            listCat = initial_catlist
                        
                        
            
        else:
            if cat[0] != '~':
                for rest in dictLoc:
                    if cat in dictLoc[rest].categories_lower:
                        for cat2 in dictLoc[rest].categories_lower:
                            listCat.append(dictLoc[rest])
                            if cat2 in cats:
                                cats[cat2] += 1
                            else:
                                cats[cat2] = 1
            
                    

    elif cat == '':
        for rest in dictLoc:
            for cat in dictLoc[rest].categories_lower:
                listCat.append(dictLoc[rest])
                if cat in cats:
                    cats[cat] += 1
                else:
                    cats[cat] = 1
    
    ordered_cats = []       
    for cat in cats:
        ordered_cats.append("\t%s (%d)" %(cat.title(), cats[cat]))
    ordered_cats.sort()
    for cat in ordered_cats:
        print cat
    
    listCat = list(set(listCat))
    
    if len(cats) == 0:
        print "Found 0 businesses, with 0 radius"
    elif len(listCat) == 1:
        print "Found 1 businesses in 0.00 radius"
        prompt = raw_input('Print the business (y/Y)? ==> ')
        print prompt
        prompt = prompt.lower()
        if prompt == 'y':
            i = 1
            for rest in listCat:
                print "%d. %s" %(i, str(rest))
        else:
            print ""
        
    else:
        initial_dist = dist(listCat[0].latitude, listCat[0].longitude, listCat[1].latitude, listCat[1].longitude)
        for rest in listCat:
            for rest2 in listCat:
                dist2 = dist(rest.latitude, rest.longitude, rest2.latitude, rest2.longitude)
                if dist2 > initial_dist:
                    initial_dist = dist2
            
        print "Found %d businesses in %.2f radius" %(len(listCat), initial_dist)
        
        prompt = raw_input('Print the business (y/Y)? ==> ')
        print prompt
        prompt = prompt.lower()
        if prompt == 'y':
            i = 1
            for rest in listCat:
                print "%d. %s" %(i, str(rest))
                i += 1
        else:
            print ""
    
    
    
                
    

if __name__ == '__main__':
    #create dictionary of restaurants with name as key and class as value
    Rdict = {}
    for line in open('businesses.json'):
        b = json.loads(line)
        r = Restaurant(b)
        if r.name in Rdict:
            count = 0
            for rest in Rdict:
                if r.name == Rdict[rest].name:
                    count += 1
            name = r.name + ' |%d' %(count)
            Rdict[name] = r
        else:
            Rdict[r.name] = r
    print '=' * 30
    while search_location() != True:
        print '=' * 30
        continue