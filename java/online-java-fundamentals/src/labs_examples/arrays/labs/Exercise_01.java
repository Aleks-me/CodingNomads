package labs_examples.arrays.labs;

import java.util.Scanner;

/**
 * Arrays calculator
 *
 *      Take in 10 numbers from the user. Place the numbers in an array. Using the loop of your choice,
 *      calculate the sum of all of the numbers in the array as well as the average.
 *
 *      Print the results to the console.
 *
 */

public class Exercise_01 {

    public static void main(String[] args) {
        int[] arr = new int[10];
        int c = 0;
        int sum = 0;
        float avg;

        System.out.println("Please, enter 10 integer numbers one by one.");
        while(c != 10){
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter " + (c+1) + " number: ");
            int number = scanner.nextInt();
            arr[c] = number;
            c++;
        }
        for(int num : arr){
            sum += num;
        }
        avg = (float) sum / 10;
        System.out.println("Sum of numbers: " + sum + ", average: " + avg);
    }
}