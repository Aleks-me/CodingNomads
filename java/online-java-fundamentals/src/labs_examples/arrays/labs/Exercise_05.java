package labs_examples.arrays.labs;

/**
 *  Traversing Arrays Backwards
 *
 *      Please create and populate an array of your choosing. Then, please demonstrate how to print out every other
 *      element in the array in reverse order.
 *
 */

public class Exercise_05 {
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
        for (int i = arr.length-1; i >= 0; i--) {
            for (int j = arr[i].length-1; j >= 0; j--) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
