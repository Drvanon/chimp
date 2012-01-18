import webbrowser

def print_a_line(name, score):
    higscore = open('highscores.txt', 'a')
    score = str(score)
    higscore.write(score)
    higscore.write('\t')
    higscore.write(name)
    higscore.write('\n')
    
def historic(score, name):
    print_a_line(name, score)

def print_all():
    a = open('highscores.txt', 'r')
    return a.read()

def print_in_browser():
    webbrowser.open('data/highscore.txt')