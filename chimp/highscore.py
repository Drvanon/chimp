def print_a_line(name, score):
    higscore = open('highscores.txt', 'a')
    score = str(score)
    higscore.write(score)
    higscore.write('\t')
    higscore.write(name)
    higscore.write('\n')
    
def historic(score, name):
    print_a_line(name, score)