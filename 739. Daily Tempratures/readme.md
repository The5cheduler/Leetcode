# Approach

1. Create the stack that will hold the value of [ temperature, index ]
2. Create another list to store the result

3. enumerate through the list of temperatures
4. check if the stack has value and compare the topmost element with the current temperature
5. if the above check satisfies then pop the topmost element from the stack and store the value in separate variables update current result at popped index with current index - popped index
6. then, add value to the stack with temperature and index

7. return result.
