class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []
        new_ls = []

        for i in range(n+1):
            x = bin(i)[2:]
            ls.append(x)

        dict = {}

        for i in ls:
            count = 0 
            j=0
            while j<len(i):
                if i[j]=='1':
                    count +=1
                j+=1

            new_ls.append(count)

        return new_ls



        