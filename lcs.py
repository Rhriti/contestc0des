

def sol(nums,k):
    def possible(guess):
        #Is there k or more pairs with distance <= guess?
        count = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > guess:
                left += 1
            count += right - left
        print(f'guess {guess} count {count}  return  {count >= k}')
        return count >= k

    nums.sort()
    lo = 38
    hi = nums[-1] - nums[0]
    while lo < hi:
        mi = (lo + hi) // 2
        if possible(mi):
            hi = mi
        else:
            lo = mi + 1
    print(lo) 
    return lo

    
 