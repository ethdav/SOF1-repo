def find_pairs(num_list, target):
    valid_pairs = []
    for i in range(len(num_list)):
        target_half = target - num_list[i]
        for j in range(i,len(num_list)):
            if num_list[j] == num_list[i]:
                pass
            elif target_half == num_list[j]:
                valid_pairs.append((num_list[i], num_list[j]))
    return valid_pairs

def main():
    target = 9
    num_list = [2,4,5,7]
    print(find_pairs(num_list, target))

main()