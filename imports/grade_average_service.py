def compute_grade(homeworks):
    total = 0
    for score in homeworks.values():
        total += score
    return round(total/len(homeworks),2)