

def computegrade(score): 



    try: 
        if score > 1: 
            grade = 'Bad Score'
        elif score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        return grade 
        
    except:
        print ('Bad Score') 
   
    score = raw_input('Enter score: ')     
    score = float(score)  
