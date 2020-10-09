package labs_examples.fundamentals.labs;

/**
 * Fundamentals Exercise 4: My Second Program
 *
 *      Write the necessary code to display declare and print each of Java's primitive data types.
 *      Please declare a single variable of each type, give it an appropriate value, then print that variable.
 *
 */

public class Exercise_04 {

    public static void main(String[] args) {

        int i = -434324324;
        System.out.println("int i is: " + i);

        // write your code below
        boolean b = true;
        char c = 'a';
        short s = -32000;
        long l = 3240923823443423423L;
        float f = 123.33f;
        double d = 12312343242341412412412412412.99999;
        byte by = 127;

        System.out.println("boolean b is: " + b);
        System.out.println("char c is: " + c);
        System.out.println("short s is: " + s);
        System.out.println("long l is: " + l);
        System.out.println("float f is: " + f);
        System.out.println("double d is: " + d);
        System.out.println("byte by is: " + by);
    }

}