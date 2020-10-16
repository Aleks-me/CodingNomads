package labs_examples.conditions_loops.labs;

/**
 * Conditions and Loops Exercise 9: break
 *
 *      Demonstrate the use of the "break" statement to exit a loop.
 *
 */

public class Exercise_09 {
    public static void main(String[] args) {

        int amount = 100;
        point:
        {
            for (int i = 0; i < 200; ){
            i += 5;
            System.out.println(i);
            if (i == amount) {
                System.out.println("Stop");
                break point;
                }
            }
        }
        System.out.println("Stopped at: " + amount);
    }
}
