with open('in2') as f:
    lines_raw = f.read().splitlines()

import hashlib
def calc_sha256(line_number: int, plain: str):
    plain_byte = bytes(plain, 'ascii')
    hashed = hashlib.sha256(plain_byte).hexdigest()
    # print(hashed)

for i,line in enumerate(lines_raw):
    calc_sha256(0, line)

