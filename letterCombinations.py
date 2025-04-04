
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []

        keys = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        result=[]

        def back(index,currcombi):
            if index==len(digits):
                result.append("".join(currcombi))
                return
            curr=int(digits[index])

            for i in keys[curr]:
                currcombi.append(i)
                back(index+1,currcombi)
                currcombi.pop()


        back(0,[])
        return result
        
