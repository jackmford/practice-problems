# beej guide to c

## ch2

- compilations has two stages -> a preprocessor and a compiler
- _preprocessor directives_ == `#include` and `#define`

## ch3

- strings are char \* in C
- C has ternary operators:
  - `y += x > 10? 17: 37;`
    - if x >10, add 17, else add 37

- `printf("The number %d is %s.\n", x, x % 2 == 0? "even": "odd");`
  - this ternary honestly reminds me of python a bit

- pre-increment syntax (`++i;`) increments the variable _before_ the expression is evaluated, post increment (`i++;`) evaluates and _then_ increments (commonly seen in the for loop)

- `%zu` is the format specifier for size_t (which is the type returned by the `sizeof` operator)

- if you don't but a `break` in a switch statement, your code will _fall through_ to the next case and on and on through the cases until a break is hit
