package labs_examples.arrays.examples;

import java.util.Arrays;

// Demonstrate an array overrun.
class ArrayErr {
    public static void main(String[] args) {
        int[] sample = new int[10];
        int x = 0;

        // generate an array overrun
        for(int i = 0; i < 10; i++){
            sample[i] = x;
            x++;
        }

        System.out.println(Arrays.toString(sample));
    }
}