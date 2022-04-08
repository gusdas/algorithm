def solution(list):
    results = []
    prev_elements = []
    name = ""
    parent = ""
    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop() #여기가 미쳤음  [2,3] 일떄 1 2 3 들어왔다가 이거때문에 3을 뺴버리고 [3] 일때 [1,2,3] 들어오고 함수 종료
    dfs(list)
    return results

list = [1,2,3]
print(solution(list))
