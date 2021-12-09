global_words =[]
global_target =''
global_answer = 987654321

def dfs(tmp_cnt, visited, begin) :
    global global_words, global_target, global_answer
    if begin == global_target :
        if tmp_cnt < global_answer :
            global_answer = tmp_cnt
        return

    for i in range(len(global_words)) :
        if not visited[i] and begin != global_words[i] :
            cnt =0
            for j in range(len(global_words[i])) : # 단어 정확히 하나 다른 것만 찾기
                if begin[j] != global_words[i][j] :
                    cnt +=1
                if cnt >= 2:
                    break
            if cnt == 1 :
                visited[i] = 1
                dfs(tmp_cnt+1,visited, global_words[i])
                visited[i] = 0
            else :
                continue

def solution(begin, target, words):
    global global_words, global_target, global_answer
    global_words, global_target = words, target
    visited = [0] * len(words)
    if target not in words :
         return 0
    else :
        dfs(0,visited, begin)

    return global_answer

# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))