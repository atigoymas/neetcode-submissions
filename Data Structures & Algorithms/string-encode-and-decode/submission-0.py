class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for val in strs:
            ans.append(str(len(val)))
            ans.append("$")
            ans.append(val)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            print(length)
            print(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j

        return ans
