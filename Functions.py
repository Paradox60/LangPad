from datetime import datetime
import datetime as date
from random import randint
import random

def Now_Time():
    current_datetime = datetime.now()

    moment1 = date.datetime(1, 1, 1, 0, 0, 0)
    moment2 = date.datetime(current_datetime.year, current_datetime.month,current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second)
    delta = moment2 - moment1

    delta_s = delta.total_seconds()
    delta_s = int(delta_s)
    return delta_s

def Gen_Num(All_Words,ran_que):
    ran_ans = []

    while True:
        for value in range(0, 3):
            ran_ans.append(random.choice(All_Words))

        if ran_ans[0] != ran_ans[1] != ran_que and ran_ans[2] != ran_ans[0] != ran_que and ran_ans[1] != ran_ans[2] != ran_que:
            break

        else:
            ran_ans = []

    return(ran_ans)

def Shuffle(ran_que,ran_ans):
    answer_list = [ran_que, ran_ans[0], ran_ans[1], ran_ans[2]]
    random.shuffle(answer_list)

    return answer_list

