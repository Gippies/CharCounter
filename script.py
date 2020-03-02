import multiprocessing


def _core_counter(lines, sender_conn):
    count_dict = {}
    for line in lines:
        for char in line:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    sender_conn.send(count_dict)


def _receiver_counter(num_of_cores, receiver_connections):
    count_dict_list = []
    for i in range(num_of_cores):
        count_dict_list.append(receiver_connections[i].recv())
    for d in count_dict_list:
        print(d)


def multi_process_counter():
    lines_dict = {}
    num_of_cores = multiprocessing.cpu_count()
    with open('input.txt') as f:
        for i, line in enumerate(f):
            core_index = i % num_of_cores
            if core_index not in lines_dict:
                lines_dict[core_index] = []
            lines_dict[core_index].append(line)

    processes = []
    receiver_connections = []
    for i in range(num_of_cores):
        receiver_conn, sender_conn = multiprocessing.Pipe(duplex=False)
        processes.append(multiprocessing.Process(target=_core_counter, args=(lines_dict[i], sender_conn)))
        receiver_connections.append(receiver_conn)

    # Create a receiver process
    processes.append(multiprocessing.Process(target=_receiver_counter, args=(num_of_cores, receiver_connections)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()


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
    multi_process_counter()
