package labs_examples.conditions_loops.labs;

import java.util.Scanner;

/**
 * Conditions and Loops Exercise 3: Months of the year
 *
 *      Take in a number from the user and print "January", "February", ... "December", or "Other"
 *      if the number from the user is 1, 2,... 12, or other respectively. Use a "switch" statement.
 *
 */

public class Exercise_03 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Please, enter a one number from 1 to 12: ");
        int enter = scan.nextInt();

        switch(enter){
            case 1:
                System.out.println("1 - January");
                break;
            case 2:
                System.out.println("2 - February");
                break;
            case 3:
                System.out.println("3 - March");
                break;
            case 4:
                System.out.println("4 - April");
                break;
            case 5:
                System.out.println("5 - May");
                break;
            case 6:
                System.out.println("6 - June");
                break;
            case 7:
                System.out.println("7 - July");
                break;
            case 8:
                System.out.println("8 - August");
                break;
            case 9:
                System.out.println("9 - September");
                break;
            case 10:
                System.out.println("10 - October");
                break;
            case 11:
                System.out.println("11 - November");
                break;
            case 12:
                System.out.println("12 - December");
                break;
            default:
                System.out.println("Enter number from 1 to 12 to convert it into month name.");
        }


    }
}
