class Solution:
    def reverseWord(self,s , k):
        a = list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)


s1= Solution()
s = "asbjle"
k = 2
ans = s1.reverseWord(s,k)
print(ans)

