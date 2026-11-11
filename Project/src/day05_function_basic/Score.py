def score(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list)/len(score_list), 1)
    return max_score, min_score, avg_score