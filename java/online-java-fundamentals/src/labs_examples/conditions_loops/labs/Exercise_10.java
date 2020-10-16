package labs_examples.conditions_loops.labs;

/**
 * Conditions and Loops Exercise 10: continue
 *
 *      Demonstrate the use of the "continue" statement to skip to the next iteration of a loop.
 *
 */

public class Exercise_10 {
    public static void main(String[] args) {

        for(int i = 10; i > 0; i--){
            for(int j = 0; j < 10; j++){
                if(i == j | i > j) continue;
                System.out.println("i and j: " + i + ":" + j);
            }
        }

    }
}
