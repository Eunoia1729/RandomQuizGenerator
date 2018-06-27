import random
import os
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
states = list(capitals.keys())
students = int( input("Enter the number of students:"))
questions =int(input("Enter the number of questions you need in each paper:"))
"""
cwd = os.getcwd()
path = os.path.join(cwd, 'questions')
os.makedirs(path)
path = os.path.join(cwd, 'key')
os.makedirs(path)
"""
for i in range(students):
    file = open('questions\question_paper_%s.txt' % ( i + 1), 'w')
    anskey = open('key\\answer_key_%s.txt' % ( i + 1), 'w')
    file.write(" Name:\n Roll number:\n Date:\n\n"+ ' '*20 + ' STATE-CAPITAL QUIZ (FORM %s)\n' %(i + 1))
    anskey.write('\n'+' '*20 + ' QUIZ ANSWER KEY (FORM %s)\n\n' %(i + 1) )
    random.shuffle(states)
    for j in range(questions):
     file.write('\n  '+ str(j + 1) + '. What is the capital of '+ states[j]+' ?\n')
     cap = list( capitals.values())
     choices = [ capitals[states[j]] ]
     cap.remove(capitals[states[j]])
     for z in range(3):
        k = random.choice(cap)
        choices.append(k)
        cap.remove(k)
     random.shuffle(choices)
     options = ['A','B','C','D']
     opt = dict( zip(choices, options) )
     for k in opt:
         file.write('   '+str(opt[k])+'. ' +str(k)+'\n')
     anskey.write('  '+str(j+1)+'. '+ str(opt[capitals[states[j]]])+'. '+ str(capitals[states[j]])+'\n')
print("question files and keys have been generated !")
