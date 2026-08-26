class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ""
        for i in strs:
            for j in i:
                print(f"j: {j}")
                l += str(ord(j))
                l += ","
            l += "|"
        print(l)
        return l

    def decode(self, st: str) -> List[str]:
        s = []
        numbers = ""
        word = ""
        print(f"s: {s}")
        for i in range(len(st)):
            if st[i] == ",":
                word += chr(int(numbers))
                numbers = ""
            elif st[i] == "|":
                print(f"Appending {word} to {s}")
                s.append(word)
                word = ""
            else:
                print(f"adding s[i]: {st[i]} to {numbers}")
                numbers += st[i]
        print(s)
        return s
