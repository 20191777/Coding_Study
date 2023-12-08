def solution(genres, plays):
    answer = []
    plays_list = {}
    genere_total_play = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in plays_list:
            plays_list[g] = [(i, p)]
        else:
            plays_list[g].append((i, p))

        if g not in genere_total_play:
            genere_total_play[g] = p
        else:
            genere_total_play[g] += p

    for (k, v) in sorted(genere_total_play.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(plays_list[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer