from collections import defaultdict, OrderedDict
from operator import itemgetter

def get_sorted(X, Y):
    Z = [x for _,x in sorted(zip(Y,X))][::-1]
    return Z

def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))


def aggregate_ranks(data, rank_num):
    
    assert rank_num == 2
    
    rank_a = data[0]
    rank_b = data[1]
    
    score = {}

    value = len(rank_a)
    for rank_element in rank_a:
        if rank_element in score:
            score[rank_element] += value
        else:
            score[rank_element] = value
        value -= 1

    value = len(rank_b)
    for rank_element in rank_b:
        if rank_element in score:
            score[rank_element] += value
        else:
            score[rank_element] = value
        value -= 1

    sort_score = OrderedDict(sorted(score.items(), key=itemgetter(1)))
    return list(sort_score.keys())[::-1]
