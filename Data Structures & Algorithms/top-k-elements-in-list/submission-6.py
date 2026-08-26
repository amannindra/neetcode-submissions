class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        # print(dict)

        # a = list(sorted(dict.items()))
        a = sorted(dict.items(), key=lambda item: item[1], reverse = True)
        print(f"sortet a: {a}")
        b = list(map(lambda x: x[0], a))

        print(f"b: {b}")



        
    
        return b[0:k]

        # return a[k-1:]
        # for i in range(k):
    
        #     l.append(dict)

        