class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i=0
        ls=[]
        while i<numRows:
            if i==0:
                ls.append([1])
            elif i==1:
                ls.append([1,1])
            else:
                #make a new list
                row = [1]
                for j in range(1, i):
                    row.append(ls[i-1][j-1]+ls[i-1][j])
                row.append(1)
                ls.append(row)

            i+=1

        print(ls)
        return ls

        