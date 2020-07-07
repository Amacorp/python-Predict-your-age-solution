def predict_age(*ages):
    return sum(a*a for a in ages)**.5//2
    
    
or


import numpy as np
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return np.sum(np.array([age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]) ** 2) ** 0.5 // 2

        Best Practices6
        Clever3
    0
    Fork
    Compare with your solution
    Link




or


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # your 
    sum = 0
    listik = [age_1**2, age_2**2, age_3**2, age_4**2, age_5**2, age_6**2, age_7**2, age_8**2]
    for i in listik:
        sum += i
    return int((sum**(1/2))//2)
