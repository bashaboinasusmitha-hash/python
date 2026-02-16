'''bitwise operators works on binary bits: 0 or 1 
example : 5 in binary:101 and 3 in binary 011,
python converts numbers to binary internally if we use binary operators
binary operators are :AND(&),OR(|),XOR(^),Left shift(<<),right shift(>>)'''
#AND(&): it prints 1 if both bits are one,else prints 0
#OR(|) : it prints 1 if any of the bits are one
#XOR(^) : it prints 0 if two bits are same
#NOT(~) : formula is ~n=(n+1)
#example:
print(4 & 6 )
print(4 | 6)
print(4 ^ 6)
print(~5)
'''left shift (<<) : left shit shifts bits to left (number of shifts depends on bits given from user,left shifts are gaining of bits)
right shift(>>) : right shift,shifts bits to right and the places of bits shifted becomes zero (right shifts are losing of bits)'''
#formula for left shift is (n<<k = n*(2^k))
a=3
b=1
print(a<<1)
#note: every left shift is multiplied by 2
'''formulae for rightshift(>>) is(n>>k = n//(2^k))
every right shift is divides by 2'''
a=16
b=2
print(a>>b)