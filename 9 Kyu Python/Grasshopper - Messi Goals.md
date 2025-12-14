# Grasshopper - Messi Goals

**Difficulty:** 9 Kyu

**Language:** Python

**Completed:** 2025-12-14

---

## Description

## Messi's Goal Total
Use variables to find the sum of the goals Messi scored in 3 competitions

## Information
Messi goal scoring statistics:

| **Competition** |	**Goals** |
|:------------|:------|
| La Liga |	43 |
| Champions League | 10 |
| Copa del Rey	| 5 |

## Task
1. Create these three variables and store the appropriate values using the table above:
- la_liga_goals
- champions_league_goals
- copa_del_rey_goals
2. Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year.

---

## Given Code

```python
la_liga_goals
champions_league_goals
copa_del_rey_goals

total_goals
```

---

## My Solution

```python
goals_record: dict[str, int] = {
    "la_liga": 43,
    "champions_league": 10,
    "copa_del_rey": 5
}

total_goals: int = sum(goals_record.values())
```

### Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)
