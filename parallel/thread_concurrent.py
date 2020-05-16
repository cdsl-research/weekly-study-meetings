import hashlib

results = []


def calc_sha256(line_number: int, plain: str):
    plain_byte = bytes(plain, 'ascii')
    hashed = hashlib.sha256(plain_byte).hexdigest()
    results[line_number] = hashed


def main():
    with open('in2') as f:
        lines_raw = f.read().splitlines()

    # for l in lines_raw:
    #     print(l)

    global results
    results = list([0] * len(lines_raw))

    from concurrent import futures as confu
    with confu.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(calc_sha256, i, line) for i, line in enumerate(lines_raw)]
        confu.wait(futures)

    # for r in results:
    #     print(r)


if __name__ == '__main__':
    main()
