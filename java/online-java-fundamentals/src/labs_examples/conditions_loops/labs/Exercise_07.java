package labs_examples.conditions_loops.labs;

import java.util.Scanner;

/**
 * Conditions and Loops Exercise 7: First vowel
 *
 *      Take in a word from the user and using a "while" loop, find the first vowel in the word.
 *      Once you find the vowel, print out the word and the first vowel.
 *
 *      Hints:
 *          - there are a few helpful methods in the String class called length(), charAt() and indexOf()
 *          - you'll likely want to use a String that contains all the vowels:
 *              - ie: String vowels = "aeiou";
 *
 */

public class Exercise_07 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Please, enter some word: ");
        String inp = scan.nextLine();

        int c = 0;
        int i = 0;
        while(c < inp.length() & i != 1){
            char ch = inp.charAt(c);
            switch(ch){
                case 'a':
                case 'A':
                case 'e':
                case 'E':
                case 'i':
                case 'I':
                case 'o':
                case 'O':
                case 'u':
                case 'U':
                    i = 1;
                    System.out.println("You entered: " + inp + ", first vowel: " + ch);
            }
            c++;
        }
        if(i == 0) {
            System.out.println("No vowels.");
        }
    }
}
