class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            # Now check if stack has something and the current stack temperature index is < the stack
            while stack and temperatures[stack[-1]]<temperatures[i]:
                # Pop the index because you found it 
                idx = stack.pop()
                result[idx]= i-idx
                
                print(result)

            # now check for i 
            stack.append(i)

        return result 
        