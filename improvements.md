# Improvements over Basic Calculator:

## Utilizes multiple classes to call operations
### 1. User interacts with Calculator class (ex: Calculator.add(#,#))
### 2. Calculator class method creates a calculation instance
### 3. Calculation class stores individual calculations dynamically, in that created instance
### 4. Calculator class calls for get result on calculation instance
### 5. Calculation class calls the corresponding operation on the stored information and returns it
### 6. Calculator class method returns the result to user

## Improvements:
### User never has to interact with or see the underlying operations
### "One point of entry" in terms of using Calculator methods

## Where it can be improved further:
### Divide by zero exception
### History of calculations
### Type hints for operation methods(improve efficiency)
### Private classes/methods for further information hiding
### Shorten methods further