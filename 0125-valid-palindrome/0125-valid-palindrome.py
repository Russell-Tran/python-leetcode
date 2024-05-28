class Solution:
    def isPalindrome(self, s: str) -> bool:
        #alphanumeric = {1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q...}
        if not s:
            return True
        
        
        front_idx = 0
        back_idx = len(s)-1
        
        s = s.lower()
        while front_idx < back_idx:
            front = s[front_idx]
            if not front.isalnum():
                front_idx += 1
                continue
            back = s[back_idx]
            if not back.isalnum():
                back_idx -= 1
                continue
            if front != back:
                return False
            front_idx += 1
            back_idx -= 1
            
        return True