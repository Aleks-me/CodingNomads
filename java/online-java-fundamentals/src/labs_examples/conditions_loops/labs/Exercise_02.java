package labs_examples.conditions_loops.labs;

import java.util.Scanner;

/**
 * Conditions and Loops Exercise 2: Days of the week
 *
 *      Take in a number from the user and print "Monday", "Tuesday", ... "Sunday", or "Other"
 *      if the number from the user is 1, 2,... 7, or other respectively. Use an if-else statement
 *      to accomplish this task.
 * 
 *      Bonus Tricky Challenge: Use a "nested-if" statement.
 *
 */

public class Exercise_02 {

    public static void main(String[] args) {

        // 1) create scanner (don't forget to import Scanner!)
        Scanner scan = new Scanner(System.in);
        // 2) prompt user
        System.out.println("Please, enter one number from 1 to 7: ");
        // 3) assign input to variable as int
        int num = scan.nextInt();
        // 4) write completed code here
        if(num == 1) {
            System.out.println("1 = Monday");
        }else if(num == 2){
            System.out.println("2 = Tuesday");
        }else if(num == 3){
            System.out.println("3 = Wednesday");
        }else if(num == 4){
            System.out.println("4 = Thursday");
        }else if(num == 5){
            System.out.println("5 = Friday");
        }else if(num == 6){
            System.out.println("6 = Saturday");
        }else if(num == 7){
            System.out.println("7 = Sunday");
        } else{
            System.out.println("Not, this is not right number!");
        }

    }
}
