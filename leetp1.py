def reverseBits(n):
    binary_representation = bin(n & 0xffffffff)[2:].zfill(32)
    reversed = binary_representation[::-1]
    ot = int(reversed,2)
    return ot

