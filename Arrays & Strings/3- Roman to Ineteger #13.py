class Solution:
    def romanToInt(self, s: str) -> int:

        d  = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 } #Hashmap for Roman Numbers

        sum = 0 # to store 
        n = len(s) #length of input String
        i = 0 #to track hashmaps' indexes

        while i < n:
            if i < n-1 and d[s[i]] < d[s[i+1]]:  # like example C < M ----> M - C
                sum+= d[s[i+1]] - d[s[i]]
                i+=2 # 2 strings as a one number
            else:
                sum+=d[s[i]]
                i+=1
            return sum # final 
    