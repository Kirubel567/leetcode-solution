class Solution:
    def smallestNumber(self, num: int) -> int:
        #sorting the digits gives the answer 
        #but the catch is that no leading zero is allowed
        #but the zero after the first number to get the smallest after sorting

        if num == 0: 
            return 0
        store = []
        negative = False
        if num < 0: 
            negative = True
            num = (num) * -1
        
        while num > 0: 
            digit = num % 10

            store.append(digit)
            num //= 10
        
        if negative: 
            store.sort(reverse = True)
        else: 
            store.sort()
        
        
        if not negative: 
            for i in range(len(store)): 
                if store[i] != 0 and store[0] == 0: 
                    store[i], store[0] = store[0], store[i]
                    break
        

        stringList = [str(num) for num in store]
        joined_str = ''.join(stringList)

        return int(joined_str) if not negative else -1 * int(joined_str)
        








