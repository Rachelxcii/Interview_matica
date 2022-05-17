# Problem title: H-index
# Kick start - Coding Practice 2022
# Language: Python 3
# Big-O Notation: O(n)

test = int(input())
test_case = 1

while test > 0:
    
    papers = int(input())
    citations = list(map(int, input().split()))
    
    h_index, position = [], 0
    count_numbers = [0]*(max(citations)+1)
    
    for num in citations:
        
        count_numbers[num] += 1
        
        if num >= position:
            if count_numbers[position] != 0:
                count_numbers[position] -= 1
            else:
                position += 1
                   
        h_index.append(str(position))
   
    print('Case #{}: {}'.format(test_case, ' '.join(h_index)))
    
    test_case += 1
    test -= 1
