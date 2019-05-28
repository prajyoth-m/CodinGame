import os


questions=[]
anxiety=0
stress=0
depression=0
with open('questionnaire.txt') as f:
    questions+=f.read().splitlines()
print('On a scale of 0-3 which indicates how much the statement applied to you over the past week.\n0 - Did not apply to me at all.\n1 - Applied to me to some degree, or some of the time.\n2 - Applied to me to a considerable degree or a good part of time.\n3 - Applied to me very much or most of the time.')
for question in questions:
    quo=question.split('=')
    print(quo[0])
    tmp=int(input("Rating: "))
    if quo[1]=='a':
        anxiety+=tmp
    elif quo[1]=='s':
        stress+=tmp
    elif quo[1]=='d':
        depression+=tmp
anxiety=anxiety*2
stress=stress*2
depression=depression*2

def getScoring(score,types)

print(anxiety,stress,depression)

