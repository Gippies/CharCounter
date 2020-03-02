

def single_process_counter():
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line)
    count_dict = {}
    for line in lines:
        for char in line:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    sorted_count = dict(sorted(count_dict.items()))
    for item in sorted_count.items():
        print(item)
    return sorted_count


if __name__ == '__main__':
    single_process_counter()
