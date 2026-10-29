# Grading rules

Marks must be a whole number from 0 to 100, inclusive.

| Marks | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

Check the conditions in descending order. For example, 85 fails `marks >= 90` but passes `marks >= 80`, so its grade is B. The remaining conditions are skipped.

Negative numbers, marks above 100, empty input, words, and decimal marks are rejected and the question is repeated. Decimal marks are not rounded. A student name must contain at least one non-space character.
