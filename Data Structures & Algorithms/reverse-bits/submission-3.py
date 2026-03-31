class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:].zfill(32)
        z = x[::-1]
        y = int(z,2)
        return y


        