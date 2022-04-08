def solution(progresses, speeds):
    answer = []
    cnt = 0  #pop 됐나 안됐나 확인 플래그
    time = 0 #날짜
    #time은 초기화가 안되니깐 반복문 돌면서 cnt만 증가하고
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt) #마지막 pop되고 반복문 중단할떄
    return answer
    # for i in len(progresses):
    #     prog = progresses[i]
    #     while prog > 100:
    #         prog += speeds[0]
    #         cnt += 1
    #     answer[i] = cnt
    #
    # return answer


print(solution([93, 30, 55], [1, 30, 5]))
