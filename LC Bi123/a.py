
def triangleType( nums=[9,4,9]) :
    if nums[0]+nums[1]>=nums[2] and nums[0]+nums[2]>=nums[1] and nums[2]+nums[1]>=nums[0]:
        if nums[0]==nums[1]==nums[2]:return "equilateral"
        elif nums[0]!= nums[1] and nums[0]!=nums[2] and nums[1]!=nums[2]:return 'scalene'
        else:return 'isosceles'
    else:
        return 'none'
print(triangleType())