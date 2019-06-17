# Shell, I/O Redirections and filters project

## Description

Scripts using special characters and I/O redirections

### First script
*Hello World*

Print 'Hello,World' `echo "Hello, World`

### Second script
*Confused smiley*

Print a confused smiley `echo "\"(Ôo)'"`

### Third script
*Let's display a file*

Print contents of a file `cat /etc/passwd`

### Forth script
*What about 2*

Print content of '/etc/passwd' and '/etc/hosts' `cat /etc/passwd /etc/hosts`

### Fifth script
*Last lines of a file*

Print the last 10 lines `tail -n 10 /etc/passwd`

### Sixth script
*I'd prefer the first ones actually*

Print the first 10 lines `head -n 10 /etc/passwd`

### Seventh script
*Line #2*

Print the third line of a file `head -n 3 iacta | tail -n 1`

### Eighth script
*It is a good file that cuts iron without making a noise*

Create a file containing the text 'Holberton School' `echo "Holberton School" > \\*\\\\\''"'Holberton\ School'"'\\\'\\\\*$\\?\\*\\*\\*\\*\\*:\)`

### Ninth script
*Save current state of directory*

Writes into a file the result of a command `ls -la > ls_cwd_content`

### Tenth script
*Duplicate last line*

Duplicate the last line of the file `tail -n 1 iacta >> iacta`

### Eleventh script
*No more javascript*

Delete al the regular files with '.js' extension in current directory as in its subfolders `find ./ -type f -name "*.js" -delete`

### Twelfth script
*Don't just count your directories, make your directories count*

Count the number of directories and sub-directories `find -mindepth 1 -type d | wc -l`

### Thirteenth script
*What's new*

Print the 10 newest files in the current directory `ls -t | head`

### Fourteenth script
*Being unique is better than being perfect*

Print only the words that appear exactly once `sort | uniq --unique`

### Fifteenth script
*It must be in that file*

Print lines containing the pattern "root" from a file `grep "root" /etc/passwd`

### Sixteenth script
*Count that word*

Print the number of lines that contains the pattern "bin" `grep "bin" /etc/passwd | wc -l`

### Seventeenth script
*What's next*

Print lines containing the pattern "root" and 3 lines after `grep -A3 "root" /etc/passwd`

### Eighteenth script
*I hate bins*

Print al the lines that do not contain the pattern "bin" `grep -v "bin" /etc/passwd`

### Nineteenth script
*Letters only please*

Print lines starting with a letter `grep -i ^[a-z] /etc/ssh/sshd_config`

### Twentieth script
*A to Z*

Replace all characters 'A' and 'c' from input to 'Z' and 'e' respectively `tr [A][c] [Z][e]`

### Twenty-first script
*Without C, you would live in hiago*

Removes all letters 'c' and 'C' from input `tr -d [c][C]`

### Twenty-second script
*esreveR*

Reverse its input `rev`

### Twenty-third script
*DJ Cut Killer*

Print all users and their home directories sorted by users `cut -d : -f 1,6 /etc/passwd | sort`

## Maintainer

@Diego-zen

## School

@HolbertoN