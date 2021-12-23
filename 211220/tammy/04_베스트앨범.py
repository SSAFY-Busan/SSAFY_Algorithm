def solution(genres, plays):
    genre_play = list(zip(genres,plays,range(0,len(genres))))
    genre_play.sort(key=lambda x:x[1], reverse=True)
    # print(genre_play)
    playlist={}
    for genrename, playnum, idx in genre_play:
        if genrename in playlist.keys():
            playlist[genrename][0] += playnum
            playlist[genrename][1].append(idx)

        else:
            playlist[genrename] = [playnum,[idx]]

    playlist_values = sorted(playlist.values(), reverse=True)
    # print(playlist_values)
    answer =[]
    for i in range(len(playlist_values)) :
        answer.append(playlist_values[i][1][0])
        if len(playlist_values[i][1]) >= 2:
            answer.append(playlist_values[i][1][1])
    # print(answer)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))