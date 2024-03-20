N = int(input())

ice_berg = [0] * 100

for i in range(N):
    ice_berg[i] = int(input())

max_hegith = max(ice_berg)

max_result = 0
for i in range(max_hegith):
    temp_ice_berg = [ ice_berg[_] for _ in range(N)]

    for j in range(N):
        if temp_ice_berg[j] - i < 0:
            temp_ice_berg[j] = 0
        else:
            temp_ice_berg[j] -= i
    
    count = 0
    bit = 0
    for check in range(N):
        if temp_ice_berg[check] != 0:
            bit = 1

        if bit == 1 and temp_ice_berg[check] == 0:
            bit = 0
            count += 1
            
        if bit == 1 and check == N-1:
            count += 1
    max_result = max(max_result, count)

print(max_result)