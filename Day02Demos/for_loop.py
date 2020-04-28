nums=[10,20,30]

#for loop

for i in nums:              #i is an element
    print i
    i=i**2

print "Nums list = ",nums   #[10,20,30]
print "========================================="

#need to get an index and its respective element inside loop: for along with range()
print range(3)              #[0,1,2]
print range(5,11)           #[5, 6, 7, 8, 9, 10]

for i in range(len(nums)):    #len(num3) -> 3  then range(3)->[0,1,2] i as an index
    print "Index = ",i," Element = ",nums[i]
    nums[i]**=2             #nums[i]=nums[i]**2

print "Nums list updated = ",nums
