package labs_examples.arrays.labs;

/**
 *  2D Array
 *
 *      Create and populate a 5x5 2D array with multiples of 3, starting with 3. Once populated, print out the results.
 *
 *      The output should look something like this:
 *
 *      3 6 9 12 15
 *      18 21 24 27 30
 *      ...
 *      ...
 *      ...
 *
 */

public class Exercise_03 {

    public static void main(String[] args) {
        int[][] arr = new int[5][5];
        int start = 3;
        int c = 1;
        // creating:
        for(int i=0; i < arr.length; i++){
            for(int j=0; j < arr[i].length; j++){
                arr[i][j] = start * c;
                c++;
            }
        }
        // printing:
        for (int[] ints : arr) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }
}
