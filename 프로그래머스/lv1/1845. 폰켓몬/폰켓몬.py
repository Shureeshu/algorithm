def solution(nums):
    N = len(nums)
    answer = min(N//2, len(set(nums)))
    return answer