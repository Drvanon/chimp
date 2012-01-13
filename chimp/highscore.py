def rewind(f):
    f.seek(0)

def print_a_line(name, score):
    higscore = open('highscores.txt', 'a')
    score = str(score)
    higscore.write(score)
    higscore.write('\t')
    higscore.write(name)
    higscore.write('\n')

def DefineFile():    
    global current_file
    current_file = open('highscores.txt', 'w')
    
def historic(score, name):
    rewind(current_file)
    print_a_line(name, score)