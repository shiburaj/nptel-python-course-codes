## **Temperature Alert System**

ClimateWatch monitors daily temperature readings collected from different regions.  
To ensure safety, the system must flag temperatures that exceed the permissible limit.

- - -

### **Problem Description**

You are given a single line of input containing **space-separated integers**, where each integer represents a temperature reading for a particular region.

A temperature is considered **unsafe** if it is **strictly greater than 50**.

- - -

### **Input Format**

*   A single line containing **space-separated integers** representing temperature readings.
    

- - -

### **Output Format**

*   If **one or more temperatures are strictly greater than 50**, print all such temperatures in the **same order as input**, separated by spaces.
    
*   If **no temperature exceeds 50**, print **`0`**.
    

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Private Test cases used for evaluation | Input | Expected Output | Actual Output | Status |
| Test Case 1 | 51 51 | 51 51 | 51 51 | Passed |
| Test Case 2 | 80 20 90 80 90 | 80 90 80 90 | 80 90 80 90 | Passed |
| Test Case 3 | 0 100 100 | 100 100 | 100 100 | Passed |

  

The due date for submitting this assignment has passed.

3 out of 3 tests passed.

You scored 100.0/100.

  

**Assignment submitted on 2026-02-04, 10:01 IST**

Your last recorded submission was :

temps = map(int, input().split(" ")) danger = \[\] for t in temps: if t > 50: danger.append(str(t)) if len(danger) == 0: print("0", end="") else: print(" ".join(danger), end="")

1

temps = map(int, input().split(" "))

2

danger = \[\]

3

for t in temps:

4

  if t \> 50:

5

    danger.append(str(t))

6

​

7

if len(danger) \== 0:

8

  print("0", end\="")

9

else:

10

  print(" ".join(danger), end\="")

createCodeMirrorEditor( 'prev\_sub', true, 1, "py3");

Sample solutions (Provided by instructor)  

Select the Language . \-- Python3

L = input().split() result = \[\] for x in L: if int(x) > 50: result.append(x) if len(result) == 0: print(0) else: print(" ".join(result))

11

1

L = input().split()

2

result = \[\]

3

​

4

for x in L:

5

    if int(x) \> 50:

6

        result.append(x)

7

​

8

if len(result) \== 0:

9

    print(0)

10

else:

11

    print(" ".join(result))

createCodeMirrorEditor( 'sol\_py3', true, 1, "py3");

  

if (! ''){ onLangChoiceChange(); }

showButterBar();
