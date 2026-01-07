#include <stdio.h>

struct Student {
    char name[50];
    int class;
    char address[100];
};

int main() {
    int n, i;

    printf("Enter number of students: ");
    scanf("%d", &n);

    // ARRAY SIZE USING n
    struct Student s[n];

    for(i = 0; i < n; i++) {
        printf("\n--- Student %d ---\n", i + 1);

        printf("Enter name: ");
        scanf("%s", s[i].name);

        printf("Enter class: ");
        scanf("%d", &s[i].class);

        printf("Enter address: ");
        scanf("%s", s[i].address);
    }

    printf("\n\n===== Student Details =====\n");

    for(i = 0; i < n; i++) {
        printf("\nStudent %d\n", i + 1);
        printf("Name    : %s\n", s[i].name);
        printf("Class   : %d\n", s[i].class);
        printf("Address : %s\n", s[i].address);
    }

    return 0;
}
