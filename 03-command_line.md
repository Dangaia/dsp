# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 1.'pwd': show current working directory path
>> 2. **mkdir**: creating a directory
>> 3. **rmdir**: deleting a director
>> 4. **touch**: creates new file inside working directory
>> 5. **rm**: deleting a file
>> 6. **mv**: renaming a file
>> 7. **ls-a**: listing hidden files
>> 8. **cp**: copying a file from one directory to another
>> 9. **echo**: print some arguments
>> 10. **ls**: list directory

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > **ls**: list directory
>> **ls -a**: lists hidden files
>> **ls -l**: lists in long format 
>> **ls -lh**: lists in long and human readable format
>> **ls -lah**: lists all files in long and human readable format
>> **ls -t**: order files and directories by time tehy were last modified
>> **ls -Glp**: does not allow display of group information using long list format and appends "/" to the end of each entry

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 1. **ls -c**: displays files by file timestamp
>> 2. **ls -F**: flags filenames
>> 3. **ls -q**: displays all nonprinting characters as ?
>> 4. **ls -r**: displays files in reverse order
>> 5. **ls -1**: displays each entry on a line

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Xargs is a command intended to execute arguments after accepting a standard input. For example, below it is used to split the output into 4 items per line: $echo a b c d e f g h i j k l m n o p q r s t u v w x y z | xargs -n 2
 

