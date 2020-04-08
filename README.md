# leetCodeSubmissions
Trying to do at least one leetcode problem a day

https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU

04/06/2020: 


https://leetcode.com/problems/two-sum

1st attempt: Brute force via two nested for loops to determine if target was met. O(n^2)  


2nd attempt: Loop through the list, if the element isn't within it, add it with key-value as (value, index). But first check if (target-curr) key is in the dictionary - if it is then we have found our two values that sum up to the pair. 

Runtime O(n), space O(n)

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

1st attempt: Brute force via two nested loops to seek max profit. O(n^2)


nth attempt: It took me a while, but I realized that I didn't need to store the max value - it served no purpose to store it while doing a linear search through the list.

It is better for max profits if you find the smallest value - hence checking the value of buy_val to see if you've found it. If you find higher values later on, check to see if it maximizes the profits by subtracting it from the small buy_val.  

Runtime O(n)


https://leetcode.com/problems/contains-duplicate/

Straightforward problem - you simply check if dup_dict contains the current item iteration and if it does, there is a duplicate. If not, then add it to the dictionary and go onto the next iteration. For python, you can also use an array and check, but I believe hashmaps would be used in theory.

Runtime O(n), space O(n)


https://leetcode.com/problems/product-of-array-except-self/

Brute force solution: Essentially you loop through the array, and if the current outer iteration matches the index in the array, you skip that multiplication. When the inner loop reaches the length of the list, it is time to update the result product array, reset the inner loop and increment the outer loop.  

Better Solution: It took a bit of out of the box thinking, I think this is sort of like a dynamic programming approach - where you build the solution for the products to the left of the current element for each index in the result array. Then, you reverse nums backwards to get the right products and multiply at that index. You can skip the very last index of the right array because the product is already 1. 

Runtime O(n), space O(1)


04/07/2020: 

https://leetcode.com/problems/maximum-subarray/

Approach: Generate an array of sum arrived to at that index - only if the sum is positive - otherwise place a 0 in the array. This is to handle the case of an array that may be like [-3, 2, 1, -7]. Your max_sum in this would be [2, 1] and your corresponding stored_sums will be [0, 2, 3, 0]. To handle the corner case with only negative numbers, you only want to include the highest negative number as part of the sum - this is kept track of in smallest_neg. If by the end of the iteration we've seen only negative numbers, then we return this smallest_neg. 