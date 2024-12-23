# L1: Set Alarm

## Instructions

Write a function named `setAlarm`/`set_alarm`/`set-alarm`/`setalarm` (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

```
employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false
```

## Given Code
```python
def set_alarm(employed, vacation):
    # Your code here
```

## My Solution
```python
def set_alarm(employed, vacation):
    # Your code here
    return True if (employed == True and vacation == False) else False
```
