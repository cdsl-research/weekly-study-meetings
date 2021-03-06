# 並列・並行プログラミング

入力テキストファイルの内容を読み取り，各行を並列にSHA256を求めて入力と同じ順序で出力する．

入力例ファイル:

- in 小さいファイル
- in2 巨大なファイル
- in3 通常サイズのファイル

行数の一覧:

```
     14 in
 128457 in2
    150 in3
```

## 実行時間

```
$ time python3 thread_threading.py
python3 thread.py  37.41s user 38.88s system 127% cpu 59.855 total

$ time python3 thread_concurrent.py
python3 thread2.py  17.28s user 7.44s system 108% cpu 22.810 total

$ time python3 serial.py
python3 serial.py  0.44s user 0.09s system 100% cpu 0.530 total

$ time python3 thread_concurrent2.py
NUM_OR_WORKER= 2
python3 thread_concurrent2.py 2  0.55s user 0.20s system 98% cpu 0.761 total


$ time python3 serial.py
python3 serial.py  0.45s user 0.19s system 98% cpu 0.650 total

$ time python3 thread_concurrent2.py 4
NUM_OR_WORKER= 4
python3 thread_concurrent2.py 4  0.88s user 0.22s system 98% cpu 1.114 total

$ time python3 thread_concurrent3.py 4
NUM_OR_WORKER= 4
python3 thread_concurrent3.py 4  0.91s user 0.52s system 172% cpu 0.822 total

$ time python3 thread_concurrent3.py 8
NUM_OR_WORKER= 8
python3 thread_concurrent3.py 8  0.89s user 0.55s system 192% cpu 0.748 total

$ time python3 thread_concurrent3.py 2
NUM_OR_WORKER= 2
python3 thread_concurrent3.py 2  0.83s user 0.45s system 128% cpu 0.994 total
```
