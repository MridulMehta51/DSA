class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
                # continue
            elif i%3==0 and i%5!=0:
                res.append("Fizz")
            elif i%3!=0 and i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            entry=""
            if i%3==0:
                entry+="Fizz"
            if i%5==0:
                entry+="Buzz"
            if not entry:
                entry+=str(i)
            res.append(entry)
        return res





        




        
