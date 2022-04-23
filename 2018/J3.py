nums = [int(x) for x in input().split()]

print('0 ' + str(nums[0]) + ' ' + str(nums[0] + nums[1]) +' '+ str(nums[0] + nums[1] + nums[2]) +' '+ str(nums[0] + nums[1] + nums[2] + nums[3]))
print(str(nums[0]) + ' 0 ' + str(nums[1]) +' '+ str(nums[1] + nums[2]) +' '+ str(nums[1] + nums[2] + nums[3]))
print(str(nums[0] + nums[1]) + ' ' + str(nums[1]) + ' 0 ' + str(nums[2]) + ' ' + str(nums[2] + nums[3]))
print(str(nums[0] + nums[1] + nums[2]) + ' ' + str(nums[1] + nums[2]) + ' ' + str(nums[2]) + ' 0 ' + str(nums[3]))
print(str(nums[0] + nums[1] + nums[2] + nums[3]) + ' ' + str(nums[1] + nums[2] + nums[3]) + ' ' + str(nums[2] + nums[3])+' ' + str(nums[3])+ ' 0')
