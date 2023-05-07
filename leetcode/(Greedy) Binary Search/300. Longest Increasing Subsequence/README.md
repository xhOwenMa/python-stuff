# 300. Longest Increasing Subsequence

Many ways to solve this, I used `Greedy binary Search` with the `bisect` module

this question is very useful!

### `bisect`

- `bisect_right(List, ele)`: return the index where inserting `ele` puts `ele` to the right of all exisitng elements that are equal to `ele`
- `bisect_left(List, ele)`
- `insort(List, ele)` functions (to insert `ele` into `List`): also have `_left` and `_right`, but they work as if inserting at `bisect_right` and `bisect_left` index respectively
