###An Introduction to Git
---

#### Installing Git 

The official website of Git has [detailed information about installing on Linux, Mac, or Windows] (http://git-scm.com/book/en/Getting-Started-Installing-Git). We will be using Ubuntu 14.04 for demonstration purposes, where you install Git using apt-get.

``` sudo apt-get install git ```

#### Initial Configuration

Let’s create a directory inside which we will be working. Alternately, you could use Git to manage one of your existing projects, in which case you would not create the demo directory as below.

```
mkdir my_git_project && cd my_git_project
```

The first step is to initialize Git in a directory. This can be done using the command ```init```, which creates a ```.git``` directory that contains all the Git-related information for your project.

![git init](/GitTutorial/img/git_init.png)
