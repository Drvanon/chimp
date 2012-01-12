def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

def DefineFile():    
    global current_file
    current_file = open('highscores.txt')

def TimesPlayed(timesplayed = 0):
    global current_line
    current_line = timesplayed
    
def historic(current_line, score, name):
    print_a_line(current_line, score, name)