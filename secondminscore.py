if __name__ == '__main__':
    namelist = []
    scorelist = []
    
    for _ in range(int(input())):
        name = input()
        namelist.append(name)
        
        score = float(input())
        scorelist.append(score)
    
    secondminscore = sorted(set(scorelist))[1]
    
    secondminscorenames = [name for name, score in zip(namelist, scorelist) if score == secondminscore]
