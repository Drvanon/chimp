def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)

def print_a_line(f, name):
    int(TimesHit)
    f.write(TimesHit, name)

def DefineFile():    
    global current_file
    current_file = open('highscores.txt', 'w')

def TimesPlayed(timesplayed = 0):
    global current_line
    current_line = timesplayed
    
def historic(score, name):
    TimesPlayed()
    rewind(current_file)
    print_a_line(score, name)