N = int(input())

max_occurrences = [0] * 26

for _ in range(N):
    a, b = input().split()

    occurrences_a = [0] * 26
    occurrences_b = [0] * 26
    
    for char in a:
        occurrences_a[ord(char) - ord('a')] += 1

    for char in b:
        occurrences_b[ord(char) - ord('a')] += 1

    for i in range(26):
        max_occurrences[i] += max(occurrences_a[i], occurrences_b[i])

for count in max_occurrences:
    print(count)