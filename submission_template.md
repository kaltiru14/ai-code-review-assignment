# AI Code Review Assignment (Python)

## Candidate
- Name: Kalkidan Belayneh Debas
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function divides by the total number of orders instead of the number of non-cancelled orders, producing an incorrect average.
- A division-by-zero error can occur when the input list is empty or when all orders are cancelled.

### Edge cases & risks
- Empty input list.
- All orders having status "cancelled".
- Missing keys such as "status" or "amount" in an order dictionary.

### Code quality / design issues
- Assumes all orders contain required keys, which can raise runtime errors.
- The logic in the code does not match the stated behavior in the explanation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track the count of non-cancelled orders separately.
- Divide the total amount only by the number of valid (non-cancelled) orders.
- Safely access dictionary keys using `.get()`.
- Return `0.0` when no valid orders exist to avoid division errors.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
- Verify correct averaging when there are both cancelled and non-cancelled orders.
- Test behavior with an empty order list.
- Test when all orders are cancelled.
- Test orders missing the "status" or "amount" keys.
- Test with floating-point and integer order amounts.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation is incorrect because the original code divides by the total number of orders, including cancelled ones.
- It does not mention failure cases such as empty input or all orders being cancelled.
### Rewritten explanation
- This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders only. It safely handles edge cases such as empty input or when no valid orders are present by returning `0.0`.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation produces incorrect results and can fail in common edge cases. Corrections are required to ensure accuracy and robustness.
- Confidence & unknowns: High confidence in the fix. The only assumption is that returning `0.0` is acceptable when no valid orders exist, as no alternative requirement was specified.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
