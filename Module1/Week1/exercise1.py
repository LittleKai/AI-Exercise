def precision(tp, fp):

    if tp == 0:
        return 0
    else:
        return tp / (tp + fp)

def recall(tp, fn):

    if tp == 0:
        return 0
    else:
        return tp / (tp + fn)

def fscore(precision, recall):

    if precision == 0 or recall == 0:
        return 0
    else:
        return 2 * (precision * recall) / (precision + recall)

def exercise1(tp, fp, fn):

    error_msg = []
    if not isinstance(tp, int):
        error_msg.append("tp must be int")
    if not isinstance(fp, int):
        error_msg.append("fp must be int")
    if not isinstance(fn, int):
        error_msg.append("fn must be int")

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than 0')
    elif error_msg:
        print(error_msg)
    else:
        pc = precision(tp,fp)
        rc = recall(tp,fn)
        print('precise = {pc}')
        print(f'recall = ', rc)
        print(f'f1-score = ', fscore(pc, rc))
        print(f'f1-score = ', round(fscore(pc, rc),2))


exercise1 ( tp =2 , fp =4 , fn =5)
exercise1(2, 3, 4)
exercise1(2, 3, 0)
exercise1(2, 3.3, 4.1)
