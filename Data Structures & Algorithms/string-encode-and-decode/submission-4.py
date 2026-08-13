class Solution:

    
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            stringLength = len(s)
            encodedString += str(stringLength) + "&" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "&":
                j += 1
            stringLength = int(s[i:j])
            string = s[j+1: j+1 + stringLength]
            decodedString.append(string)
            i = j + 1 + stringLength 

        return decodedString
