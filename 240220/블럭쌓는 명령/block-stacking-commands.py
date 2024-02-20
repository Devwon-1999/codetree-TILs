from collections import defaultdict

N, K = map(int, input().split())

commands = defaultdict(int)  # 명령의 범위를 기록할 딕셔너리

for _ in range(K):
    a, b = map(int, input().split())
    commands[a] += 1
    commands[b + 1] -= 1  # 범위의 끝 다음 인덱스에 -1을 기록하여 범위를 표시

blocks = [0] * (N + 1)  # 블록의 높이를 기록할 배열
current_blocks = 0  # 현재 높이의 블록 수
mid_index = N // 2  # 중앙 인덱스

for i in range(1, N + 1):
    current_blocks += commands[i]
    blocks[i] = current_blocks

# 블록의 높이 배열을 정렬하고 중앙 값을 출력
blocks.pop()
sorted_blocks = sorted(blocks)
print(sorted_blocks[mid_index])