
// There is not gcc id donwloaded to run the c file. 

# include <stdio.h>
int fibonacciSequence(int num);
int main () {
    int a = 0,b = 1 ,c = 0, n; 
    printf("Enter the number : ");
    scanf("%d", &n);
    // printf("Fibonacci of %d is %d\n", n, fibonacciSequence(n));
    printf("The fibonacci suquence %d is  %d is : ", a,b);
    c = a + b;
   
    while (c <= n){
        printf("%d", c);
        a = b;
        b = c; 
        c = a + b;
    }
    
    return 0;
}

// Fibonacci sequence... By usin the C. 
int fibonacciSequence(int num){
    if (num <= 1)
        return num;
    return fibonacciSequence(num - 1) + fibonacciSequence(num - 2); 
}