def denominators(n: int) -> list[int]:
    return [i for i in range(1, n+1) if n%i == 0]

def gcds(nums: list[int]) -> list:    
    gcd_list: list[int] = []

    # start with smallest number
    nums.sort()

    # nothing but 0 is divisible by 0
    if nums[0] == 0:
        return gcd_list

    gcd_list = denominators(nums.pop())

    for n in nums:
        if n == 0:
            return []

        gcd_list = [1] + [
            common_denominator 
            for common_denominator in gcd_list
            if n % common_denominator == 0
        ]
        
        if len(gcd_list) == 1:
            break

    return gcd_list