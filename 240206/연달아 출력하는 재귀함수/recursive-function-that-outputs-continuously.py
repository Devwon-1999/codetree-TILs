def generate_sequence(n, current=1):
    if current < 3:
        return [current]
    
    quotient = current // 3
    sequence = generate_sequence(n, quotient)
    sequence.append(current)
    return sequence

def print_sequence(sequence):
    if sequence:
        print(sequence[0], end=' ')
        print_sequence(sequence[1:])

n = int(input())
sequence = generate_sequence(n)
print_sequence(sequence)