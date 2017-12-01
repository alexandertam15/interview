'''Alex Tam'''
from collections import namedtuple
import datetime

example = []
if type(Interview) == namedtuple:
    print(example)
#type defined
Set = namedtuple('Title','Event Date Begin End')
Interview = Set('Interview at The Portal', datetime.date(2017,2,23), datetime.time(hour=15),datetime.time(hour=16,minute=30))
Cindy = Set('Lunch with Cindy', datetime.date(2017,2,25), datetime.time(hour=12),datetime.time(hour=13))
John = Set('Dinner with John', datetime.date(2017,2,24), datetime.time(hour=17),datetime.time(hour=17,minute=30))
Conference = Set('Conference', datetime.date(2017,2,24), datetime.time(hour=11),datetime.time(hour=17,minute=30))
Soccer = Set('Soccer', datetime.date(2017,2,26), datetime.time(hour=15),datetime.time(hour=16,minute=30))
Date = Set('Date', datetime.date(2017,2,23), datetime.time(hour=15),datetime.time(hour=16,minute=30))
Wedding = Set('Wedding', datetime.date(2017,2,27), datetime.time(hour=14),datetime.time(hour=16,minute=30))
Class = Set('Class', datetime.date(2017,2,23), datetime.time(hour=14),datetime.time(hour=16))



TotalEvents=[Set, Interview,Cindy,John,Conference,Soccer,Date,Wedding,Class]
'''list of all the events '''

def checker(schedulelist: list)->list:
    '''takes a list of events and will return all the events that overlap in time'''
    counter = 0
    inter=[]
    finallist=[]
    listtype=[]
    fulllist = []
    difflist = schedulelist
    for set2 in schedulelist:
        for set1 in difflist:
            if not(set1==set2):
                if set1.Date == set2.Date:
                    if (set2.Begin < set1.End and set1.Begin < set2.End):
                        fulllist.append(set1)
    for name in fulllist:
        if not(name.Event in finallist):
            if (name in schedulelist):
                finallist.append(name.Event)
    return finallist

if __name__ == "__main__":
    '''call checker function with list of all the events'''
    print(checker(TotalEvents))



