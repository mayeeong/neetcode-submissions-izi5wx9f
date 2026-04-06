class Solution:
    def encode(self, strs: List[str]) -> str:
        encoder = ""
        i=0
        while i<len(strs):
            length = len(strs[i])
            encoder += f"{length}#{strs[i]}"
            i+=1
        return encoder


    def decode(self, s: str) -> List[str]:
        i=0
        ls = []
        while i<len(s):
            string = ""
            
            if s[i].isdigit():
                j = i
                while s[j].isdigit():  # ✅ read ALL digit characters
                    j += 1
                num = int(s[i:j])      # ✅ full number e.g. 10, 11, 12...
                string = s[j+1:j+1+num]  # skip the '#' then grab num chars
                ls.append(string)
                i = j + 1 + num        # ✅ move past digit(s) + '#' + word
                continue
            elif s[i]=='0' and s[i+1]=='#':
                ls.append("")
                i+=2
                continue 
            i+=1
        return ls

