def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)

def print_a_line(name, score):
    higscore = open('highscores.txt', 'w')
    score = str(score)
    higscore.write(score)
    higscore.write('\t')
    higscore.write(name)

def DefineFile():    
    global current_file
    current_file = open('highscores.txt', 'w')

def TimesPlayed(timesplayed = 0):
    global current_line
    current_line = timesplayed
    
def historic(score, name):
    TimesPlayed()
    rewind(current_file)
    print_a_line(name, score)
    
def newline():
    h = open('highscore.txt', 'w')
    h.write('\n')