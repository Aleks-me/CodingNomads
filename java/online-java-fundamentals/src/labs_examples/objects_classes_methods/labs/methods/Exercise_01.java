package labs_examples.objects_classes_methods.labs.methods;

import java.lang.reflect.Array;

/**
 * Created by ryandesmond - https://codingnomads.co
 */
public class Exercise_01 {

    public static void main(String[] args) {

        // please create the methods as instructed below then
        // call each of those methods from here, within the main()
        System.out.println(multiply(2,10));
        System.out.println(divide(100, 2));
        joke();
        System.out.println(secondsInYears(5));
        System.out.println(varChars('w', 'o', 'r', 'd'));
    }

    // 1) Create a static multiply() method below that takes two int arguments (int a, int b) and
    //    returns the result of a * b
    static int multiply(int a, int b){
        return a * b;
    }

    // 2) Create a static divide() method below that takes two int arguments (int a, int b) and
    //    returns the result of a / b
    static int divide(int a, int b){
        return a / b;
    }

    // 3) Create a static void method that will print of joke of your choice to the console
    static void joke(){
        System.out.println("I want to work in Italy so everybody will call me a senjor developer.");
    }

    // 4) Create a static method that takes in a number in years (int years) as an argument
    //    and returns the number of seconds that number in years represents
    static long secondsInYears(int y){
        if(y >= 0) return (long)(60*24*365*y);
        else return -1;
    }

    // 5) Create a varargs method that will return the length of the varargs array passed in
    static int varChars(char...c){
        return c.length;
    }
}
