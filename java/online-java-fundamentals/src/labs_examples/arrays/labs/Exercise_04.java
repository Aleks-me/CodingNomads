package labs_examples.arrays.labs;

import java.util.Arrays;

/**
 *  Irregular Arrays
 *
 *      Create and populate a 2 dimensional irregular array of size and contents of your choosing. Using a nested
 *      "for-each" loop, iterate and print out each element of the array.
 *
 */

public class Exercise_04 {

    public static void main(String[] args) {
        int[][] arr1 = new int[3][]; // 2D irregular array
        // Creating some space inside
        for (int i=0; i<3; i++) {
            arr1[i] = new int[i * 2 + 1];
        }
        System.out.println(Arrays.deepToString(arr1)); // spacing result
        // populate
        for (int i=0; i<3; i++) {
            for (int j = 0; j < arr1[i].length; j++) {
                arr1[i][j] = i * 3 + j;
            }
        }
        // print
        for (int[] ints : arr1) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }

        System.out.println();
        // same for the second array
        int[][][] arr2 = new int[3][4][]; // 3D irregular array
        for (int i=0; i<3; i++) {
            for (int j = 0; j < 4; j++) {
                arr2[i][j] = new int[(i + 1) * (j + 1)];
            }
        }
        System.out.println(Arrays.deepToString(arr2));
        for (int i=0; i<3; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < arr2[i][j].length; k++) {
                    arr2[i][j][k] = i + j + k;
                }
            }
        }
        for (int[][] ints : arr2) {
            for (int[] anInt : ints) {
                for (int annInt : anInt) {
                    System.out.print(annInt + " ");
                }
                System.out.println();
            }
        }
    }
}
