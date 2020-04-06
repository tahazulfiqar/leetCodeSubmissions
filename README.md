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