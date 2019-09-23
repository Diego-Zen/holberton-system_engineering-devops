# Shell, init files, variables and filters project

## Description

Examples of how use local and global variables, how to use expansions and special parameters and finallly how to create alias and perform aritmethic operations

* `printenv`
* `set`
* `unset`
* `export`
* `alias`
* `unalias`
* `.`
* `source`
* `printf`

### First script
*<o>*

Create an alias `alias ls='rm *'`

### Second script
*Hello you*

Print "hello user" where user is the current Linus user `echo "hello" $USER`

### Third script
*The path to success*

Add "/action" to the PATH `PATH=$PATH:/action`

### Forth script
*Path*

Count the number of directories in the PATH `echo $PATH | tr ':' '\n' | wc -l`

### Fifth script
*Global variables*

List environment varables `printenv`

### Sixth script
*Local variables*

List all local variables and environment variables, and functions `set`

### Seventh script
*Local variable*

Create a new local variable `BETTY="Holberton"`

### Eighth script
*Global variable*

Create a new global variable `export HOLBERTON="Betty"`

### Ninth script
*Addition*

Print the result of addition of 128 with an environment variable `echo $(($TRUEKNOWLEDGE + 128))`

### Tenth script
*Divide and rule*

Print the result of POWER divided by DIVIDE `echo $(($POWER / $DIVIDE))`

### Eleventh script
*Love and exponential*

Print the result of BREATH to the power LOVE `echo $((BREATH**LOVE))`

### Twelfth script
*Binary*

Convert a number from base 2 to base 10 `echo "$((2#$BINARY))"`

### Thirteenth script
*Combination*

Prints all posible combinations of two letters except 'oo' `printf '%s\n' {a..z}{a..z} | grep -v "oo"`

### Fourteenth script
*Floats*

Print a number with two decimal places `printf '%.2f\n' $NUM`

### Fifteenth script
*Decimal to Hexadecimal*

Convert a number from base 10 to base 16 `printf '%x\n' "$((10#$DECIMAL))"`

## Maintainer

@diegozencode

## School

@Holberton School