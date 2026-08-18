#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static double read_double(const char *prompt) {
    char buf[128];
    char *endptr;
    double val;

    while (1) {
        printf("%s", prompt);
        if (!fgets(buf, sizeof(buf), stdin)) {
            printf("Error reading input. Exiting.\n");
            exit(EXIT_FAILURE);
        }
        // remove trailing newline
        buf[strcspn(buf, "\n")] = '\0';
        if (strlen(buf) == 0) {
            printf("Please enter a number.\n");
            continue;
        }
        val = strtod(buf, &endptr);
        if (endptr == buf || *endptr != '\0') {
            printf("Invalid number, try again.\n");
            continue;
        }
        return val;
    }
}

int main(void) {
    char choice[16];
    printf("Simple C Calculator\n");

    for (;;) {
        printf("\nSelect an operation:\n");
        printf("  1) Add (+)\n");
        printf("  2) Subtract (-)\n");
        printf("  3) Multiply (*)\n");
        printf("  4) Divide (/)\n");
        printf("  5) Power (^ )\n");
        printf("  6) Square root (sqrt) [single operand]\n");
        printf("  7) Exit\n");
        printf("Choice: ");

        if (!fgets(choice, sizeof(choice), stdin)) {
            printf("\nGoodbye\n");
            break;
        }

        // trim
        choice[strcspn(choice, "\n")] = '\0';
        if (strlen(choice) == 0) {
            continue;
        }

        if (strcmp(choice, "1") == 0 || strcmp(choice, "+") == 0) {
            double a = read_double("Enter first number: ");
            double b = read_double("Enter second number: ");
            printf("Result: %g\n", a + b);
        } else if (strcmp(choice, "2") == 0 || strcmp(choice, "-") == 0) {
            double a = read_double("Enter first number: ");
            double b = read_double("Enter second number: ");
            printf("Result: %g\n", a - b);
        } else if (strcmp(choice, "3") == 0 || strcmp(choice, "*") == 0) {
            double a = read_double("Enter first number: ");
            double b = read_double("Enter second number: ");
            printf("Result: %g\n", a * b);
        } else if (strcmp(choice, "4") == 0 || strcmp(choice, "/") == 0) {
            double a = read_double("Enter first number: ");
            double b = read_double("Enter second number: ");
            if (b == 0.0) {
                printf("Error: Division by zero is not allowed.\n");
            } else {
                printf("Result: %g\n", a / b);
            }
        } else if (strcmp(choice, "5") == 0 || strcmp(choice, "^") == 0) {
            double a = read_double("Enter base: ");
            double b = read_double("Enter exponent: ");
            printf("Result: %g\n", pow(a, b));
        } else if (strcmp(choice, "6") == 0) {
            double a = read_double("Enter number: ");
            if (a < 0.0) {
                printf("Error: square root of negative number is not supported (returning nan).\n");
            }
            printf("Result: %g\n", sqrt(a));
        } else if (strcmp(choice, "7") == 0 || strcasecmp(choice, "q") == 0 || strcasecmp(choice, "exit") == 0) {
            printf("Exiting. Goodbye!\n");
            break;
        } else {
            printf("Invalid choice. Please enter a number from the menu.\n");
        }
    }

    return 0;
}
