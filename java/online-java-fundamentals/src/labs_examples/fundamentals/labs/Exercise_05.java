package labs_examples.fundamentals.labs;


/**
 * Fundamentals Exercise 5: Working with Strings
 *
 *      Please follow the instructions in the comments below
 *
 */

public class Exercise_05 {

    public static void main(String[] args) {

        String str = "hello!";
        // please declare an int variable below, and set it to the value of the length of "str"
        int len = str.length();
        System.out.println("str length is " + len);

        String str2 = "hello";
        // please initialize a boolean variable and test whether str is equal to str2
        boolean test = str.equals(str2);
        System.out.println("str equals str2? " + test);

        // please concatenate str & str2 and set the result to a new String variable below
        String result = str + str2;
        System.out.println("Strings together are: " + result);

        // please demonstrate the use of any other method that is available to us in the String class
        // for example, replace(), substring(), contains(), indexOf() etc
        char old = 'o';
        char new_one = 's';
        String repl = str.replace(old, new_one);
        System.out.println("Trying replace: old string - " + str + ", new string - " + repl);

    }

}