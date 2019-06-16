# Shell permissions project

## Description

Create some scripts using commands related with permissions

### First script
*My name is betty*

Changes the user ID 'su name_user'

### Second script
*Who am I*

Print userid current user 'whoami'

### Third script
*Groups*

Print all groups the current user is part of 'groups'

### Forth script
*New owner*

Change the owner of the file 'chown' you some_file'

### Fifth script
*Empty!*

Creates an empty file called hello 'touch hello'

### Sixth script
*Execute*

Adds execute permissions to file hello 'chmod u+x hello'

### Seventh script
*Multiple permissions*

Adds multiple permissions to hello file 'chmod ug+x,o+r hello'

### Eighth script
*Everybody*

Adds execution permissions to everyone to the file hello 'chmod ugo+x hello'

### Ninth script
*James Bond*

Set permission as 007 'chmod 007 hello'

### Tenth script
*John Doe*

Set specific permissions 'chmod 753 hello'

### Eleventh script
*Look in the mirror*

Set same permission to files 'chmod --reference=olleh hello'

### Twelfth script
*Directories*

Adds execute permissions to all subdirectories 'chmod -R ugo+X *'

### Thirteenth script
*More directories*

Create a directory with permissions 751 'mkdir -m 751 dir_holberton'

### Fourteenth script
*Change group*

Changes the group owner 'chgrp holberton hello'

### Fifteenth script
*Owner and group*

Changes the owner an group owner for all files and directories 'chown -R betty:holberton .'

### Sixteenth script
*Symbolic links*

Changes the owner and the group of symbolic file 'chown -h betty:holberton _hello'

### Seventeenth script
*If only*

Changes owner of file only if 'chown --from=guillaume betty hello'

## Maintainer

@Diego-zen

## School

@HolbertoN