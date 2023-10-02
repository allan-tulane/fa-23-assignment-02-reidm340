# CMPS 2200 Assignment 2

**Name:**_________________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  since $a/f(b)=2/1$, leaf dominated
.  
.  last row has $2^{log_3(n)}$ nodes
.  
.  $W(n)=O(n^{log_3(2)})$
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  since $a/f(b)=5/4$, leaf dominated
.  
.  last row has $5^{log_4(n)}$ nodes
.  
.  $W(n)=O(n^{log_4(5)})$
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  since $a/f(b)=7/7=1$, balanced
.  
.  max cost = n
.  
.  tree depth = $log_7(n)$
.  
.  $W(n)=O(nlog_7(n))$
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  since $a/f(b)=9/9=1$, balanced
.  
.  max cost = $n^2$
.  
.  tree depth = $log_3(n)$
.  
.  $W(n)=O(n^2log_3(n))$
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  since $a/f(b)=8/8=1$, balanced
.  
.  max cost = $n^3$
.  
.  tree depth = $log_2(n)$
.  
.  $W(n)=O(n^2log_2(n))$
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  since $a/f(b)=49/(25^(3/2)log(25))<1$, root dominated
.  
.  $W(n)=O(n^{3/2}log(n))$
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  tree depth = n
.  
.  max cost = 2
.  
.  $W(n)=O(2n)=O(n)$
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.  tree depth = n
.  
.  max cost = $n^c$
.  
.  $W(n)=O(nn^c)$
.  
.  
  * $W(n)=W(\sqrt{n})+1$
.  
.  $W(n)=O(log(log(n)))$


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
      .  
      .  $W(n)=5W(n/2)+n$
      .  
      .  since $a/f(b)=5/2$, leaf dominated
      .  
      .  last row has $5^{log_2(n)}$ nodes
      .  
      .  $W(n)=O(n^{log_2(5)})$
      .  
      .  
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
      .  
      .  $W(n)=2W(n-1)+1$
      .  
      .  leaf dominated
      .  
      .  last row has $2^n$ nodes
      .  
      .  $W(n)=O(2^n)$
      .  
      .  
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.
      .  
      .  $W(n)=9W(n/3)+n^2$
      .  
      .  since $a/f(b)=9/9=1$, balanced
      .  
      .  max cost = $n^2$
      .  
      .  tree depth = $log_3(n)$
      .  
      .  $W(n)=O(n^2log_3(n))$

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?
    .  
    .  I would choose #1 > #3 > #2
    .  
    .  


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


