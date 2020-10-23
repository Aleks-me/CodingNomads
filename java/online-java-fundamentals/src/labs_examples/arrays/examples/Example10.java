package labs_examples.arrays.examples;

// Use the length array member.
class LengthDemo {
    public static void main(String[] args) {

        int[][] table = { // a variable-length table
                {1, 2, 3},
                {4, 5},
                {6, 7, 8, 9}
        };

        for (int[] ints : table) {
            for (int anInt : ints) {
                System.out.println(anInt);
            }
        }
    }
}
