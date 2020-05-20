import random

#User input  
verbs = input('Number of verbs: ')
adverbs = input('Number of adverbs: ')
nouns = input('Number of nouns: ')
adjk = input('Number of adjectives: ')

f = open("adj.txt", "r") #opens word list

m = f.readlines() #reads amount of lines in file
l = []
n = []

for x in range(int(adjk)): #how many words needed 
    for i in range(0, len(m)-1): #range of document
        x = m[i] #
        z = len(x)
        a = x[:z-1]
        l.append(a)
               
    l.append(m[i+1])
    o = random.choice(l)
    n.append(o)
print("Adjectives are: " + str(n))

f.close()

f = open("adv.txt", "r")

m = f.readlines()
l = []
n = []

for x in range(int(adverbs)):
    for i in range(0, len(m)-1):
        x = m[i] #chooses corrisponding word from list
        z = len(x) #length of word
        a = x[:z-1] #word minus \n
        l.append(a) #adds chosen word to l
               
    l.append(m[i+1]) 
    o = random.choice(l) #random choice from l
    n.append(o) #adds choice to n
print("Adverbs are: " + str(n))

f.close()

f = open("noun.txt", "r")

m = f.readlines()
l = []
n = []

for x in range(int(nouns)):
    for i in range(0, len(m)-1):
        x = m[i]
        z = len(x)
        a = x[:z-1]
        l.append(a)
               
    l.append(m[i+1])
    o = random.choice(l)
    n.append(o)
print("Nouns are: " + str(n))

f.close()

f = open("verb.txt", "r")

m = f.readlines()
l = []
n = []

for x in range(int(verbs)):
    for i in range(0, len(m)-1):
        x = m[i]
        z = len(x)
        a = x[:z-1]
        l.append(a)
               
    l.append(m[i+1])
    o = random.choice(l)
    n.append(o)
print("Verbs are: " + str(n))

f.close()
