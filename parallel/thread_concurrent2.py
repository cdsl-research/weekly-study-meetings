import hashlib

results = []


def calc_sha256(line_number_begin: int, plain_lines: list):
    for line in plain_lines:
        plain_byte = bytes(line, 'ascii')
        hashed = hashlib.sha256(plain_byte).hexdigest()
        results[line_number_begin] = hashed
        line_number_begin += 1


def main():
    with open('in2') as f:
        lines_raw = f.read().splitlines()

    # for l in lines_raw:
    #     print(l)

    global results
    results = list([0] * len(lines_raw))

    import sys
    if int(sys.argv[1]) > 0:
        print("NUM_OR_WORKER=", sys.argv[1])
        NUM_OF_WORKER = int(sys.argv[1])
    else:
        NUM_OF_WORKER = 3
    CHUNK_SIZE = len(lines_raw) // NUM_OF_WORKER

    from concurrent import futures as confu
    with confu.ThreadPoolExecutor(max_workers=NUM_OF_WORKER) as executor:
        futures = [
            executor.submit(calc_sha256, i, lines_raw[i:i+CHUNK_SIZE])  for i in range(0, len(lines_raw), CHUNK_SIZE)
        ]
        confu.wait(futures)

    # for r in results:
    #     print(r)


if __name__ == '__main__':
    main()
