def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]  #다리길이
    bridge_weight = 0                           #다리위에 무게
    while len(bridge) != 0:
        time += 1

        bridge_weight -= bridge[0]
        bridge.pop(0)

        if truck_weights:
            if bridge_weight + truck_weights[0]  <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time
a = 100
b = 100
c = [10]

print(solution(a,b,c))


