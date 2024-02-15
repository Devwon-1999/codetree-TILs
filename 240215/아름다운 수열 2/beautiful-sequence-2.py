N, M = map(int, input().split())

N_List = list(map(int, input().split()))
M_List = list(map(int, input().split()))

def generate_permutations(elements):
    if len(elements) == 1:
        return [elements]
    else:
        result = []
        for i in range(len(elements)):
            first_element = elements[i]
            remaining_elements = elements[:i] + elements[i+1:]
            for permutation in generate_permutations(remaining_elements):
                result.append([first_element] + permutation)
        return result

Avalibale_M_List = generate_permutations(M_List)
answer = 0

for i in range(N - M + 1):
    temp = []
    for j in range(i, i + M):
        temp.append(N_List[j])
    if temp in Avalibale_M_List:
        answer += 1

print(answer)