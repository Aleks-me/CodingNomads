package labs_examples.datatypes_operators.labs;

/**
 * Please demonstrate the use of all arithmetic operators below. These include:
 *
 * addition, subtraction, multiplication, division and modulus
 *
 */
class ArithmeticOperators {

    public static void main(String[] args) {

        // write your code below
        int c = 5;
        long x = c + c;
        double z = c - c;
        float h = (float) c * c * c;
        short k = (short) ((c+1) / 2);
        byte l = (byte) (c % 2);

        System.out.println(x);
        System.out.println(z);
        System.out.println(h);
        System.out.println(k);
        System.out.println(l);

    }

}
