def solution(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            answer.append(path)
            return

        for i in range(index, len(digits)): #index: 입력된 숫자 갯수 만큼
            for j in dic[digits[i]]: #문자열도 배열이니깐 문자열의 index로 키값으로 dic에서 가져온다.
                dfs(i + 1, path + j) #path에 j(키 값으로 찾은 dic의 문자)

    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    answer = []
    dfs(0, "")
    return answer


print(solution("24"))
