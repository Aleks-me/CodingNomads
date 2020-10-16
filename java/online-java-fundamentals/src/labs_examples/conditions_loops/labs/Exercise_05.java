package labs_examples.conditions_loops.labs;

import java.util.Scanner;

/**
 * Conditions and Loops Exercise 5: Calculator
 *
 *      Take two numbers from the user, an upper and lower bound. Using a "for-loop", calculate the sum
 *      of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
 *      Print the results to the console.
 *
 *      For example, if a user enters 1 and 100, the output should be:
 *
 *      The sum is: 5050
 *      The average is: 50.5
 *
 *
 */

public class Exercise_05 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int inp1 = scan.nextInt();
        System.out.println("Enter second number: ");
        int inp2 = scan.nextInt();

        int counter = 0;
        for(int i = inp1; i < (inp2+1); i++){
            counter += i;
        }

        float avg = (inp1 + inp2) / 2.0f;

        System.out.println("Sum of numbers between: " + counter + ", average: " + avg);

    }
}
