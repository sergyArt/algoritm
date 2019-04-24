# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib

s = "kgfghfg"

#print(hashlib.sha1(b"ga").hexdigest())
#print(hashlib.sha1(b"ag").hexdigest())

count = []

for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        count.append(hashlib.sha1("".join(s[i:j]).encode("ascii")).hexdigest())


print("Value of substr with different hech: ", len(list(set(count))))


# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):

        code[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

def main():
    s = "good morning sergy"
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(s)
    print(encoded)

if __name__ == "__main__":
    main()
