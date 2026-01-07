
// There is not gcc id donwloaded to run the c file. 

# include <stdio.h>
int fibonacciSequence(int num);
int main () {
    int n; 
    printf("Enter the number : ");
    scanf("%d", &n);
    // printf("Fibonacci of %d is %d\n", n, fibonacciSequence(n));

    
    return 0;
}


// Fibonacci sequence... By usin the C. 
int fibonacciSequence(int num){
    if (num <= 1)
        return num;
    return fibonacciSequence(num - 1) + fibonacciSequence(num - 2); 
}