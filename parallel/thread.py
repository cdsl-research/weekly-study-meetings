import hashlib
import threading

lock = threading.Lock()
results = []


def calc_sha256(line_number: int, plain: str):
    plain_byte = bytes(plain, 'ascii')
    hashed = hashlib.sha256(plain_byte).hexdigest()

    lock.acquire()
    results[line_number] = hashed
    lock.release()


def main():
    with open('in2') as f:
        lines_raw = f.read().splitlines()

    global results
    results = list([0] * len(lines_raw))

    # for l in lines_raw:
    #     print(l)

    for i, line in enumerate(lines_raw):
        t = threading.Thread(target=calc_sha256, args=(i, line))
        t.start()
        # print("execute:", t)

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            # print("wait:", t.name)
            t.join()

    # for r in results:
    #     print(r)


if __name__ == '__main__':
    main()
