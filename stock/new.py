from BagOfWords import news_prediction

def check_result():
    result = news_prediction()
    count1 = 0
    count0 = 0
    count = 0
    
    for i in range(len(result)):
        if result[i] == 1:
            count1 = count1 + 1
        elif result[i] == 0:
            count0 = count0 + 1
        else:
            count = count + 1
    if (count1 > count0) and (count1 > count):
        print("The Nepse index will increase")
    elif (count0 > count1) and (count0 > count):
        print("The Nepse index remain same")
    else:
        print("The Nepse index will decrease")

check_result()