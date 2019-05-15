def ip_to_int32(ip):
    nums = ip.split('.')
    nums = [int(x) for x in nums]
    final = str() 
    final_int = 0
    for num in nums:
        oct = 128
        for _ in range(8):
            if num > oct:
                final += '1' 
                num -= oct
            else:
                final += '0'
            oct = oct/2
        final_int += int(final)
    return final_int

print(ip_to_int32('128.114.17.104'))