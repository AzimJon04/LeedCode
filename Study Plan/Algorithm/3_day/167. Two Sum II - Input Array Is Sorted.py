class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            l, r = i+1, len(numbers)-1
            ora = target - numbers[i]
            while l <= r:
                ort = l + (r - l)//2
                if numbers[ort] == ora:
                    return [i+1, ort+1]
                    continue
                elif numbers[ort] < ora:
                    l = ort+  1
                else:
                    r = ort - 1