#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:57:36 2018

@author: nakau
"""
from math import sqrt

critics = {
        'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My luck': 3.0, 'Superman Returns':3.5, 'You, Me and Dupree':2.5, 'The Night Listener':3.0},
        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My luck': 1.5, 'Superman Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener':3.0},
        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns':3.5, 'The Night Listener':4.0},
        'Claudia Puig': {'Snakes on a Plane': 3.5,'Just My luck': 3.0, 'Superman Returns':4.0, 'You, Me and Dupree':2.5, 'The Night Listener':4.5},
        'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My luck': 2.0, 'Superman Returns':3.0, 'You, Me and Dupree':2.0, 'The Night Listener':3.0},
        'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener':3.0},
        'Toby': { 'Snakes on a Plane': 4.5,'Superman Returns':4.0, 'You, Me and Dupree':1.0}
        }

def sim_distance(prefs, person1, person2):
    si= {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    
    n=len(si)
    if n==0: return 0
    
    sum_of_squares= sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    
    return 1/(1+sqrt(sum_of_squares))


def sim_person(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1
        
    n=len(si)
    if n==0 :return 1
    
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    
    sum1sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2sq=sum([pow(prefs[p2][it],2) for it in si])
    
    psum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    num=psum-(sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0 :return 0
    r= num/den
    
    return r

def topMatches(prefs,person,similarity=sim_person):
    scores=[(similarity(critics,person,other),other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:len(scores)]


def getRecommendations(prefs,person,similarity=sim_person):
    totals={}
    simsums={}
    for other in prefs:
        if other==person :continue
        sim =similarity(prefs,person,other)
        
        if sim<=0:continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item] +=prefs[other][item]*sim
                simsums.setdefault(item,0)
                simsums[item] +=sim
    rankings=[(total/simsums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

print(getRecommendations(critics,'Toby'))

def tansformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[item][person]
    return result

     











