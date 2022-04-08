def solution(dirs):
    visited = []  # idx = row, val = col
    answer = 0  # 처음 걸어본 길이
    x, y, nx, ny = 0, 0, 0, 0

    stack = set()
    for c in dirs:
        if c == "U":
            ny += 1
        elif c == "D":
            ny -= 1
        elif c == "L":
            nx -= 1
        elif c == "R":
            nx += 1
        if abs(nx) > 5 or abs(ny) > 5:
            nx, ny = x, y ## 5가 넘으면 과거 좌표로 변경
            continue
        if (x, y, nx, ny) not in stack:  #저장할 좌표가 없으면 저장
            stack.add((x, y, nx, ny)) #현재에서 다음 움직임 저장
            stack.add((nx, ny, x, y)) # 과거 저장
            answer += 1
        x, y = nx, ny #현재 좌표 과거로 변경
        print(stack)
    return answer


print(solution("ULURRDLLU"))
