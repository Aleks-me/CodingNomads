package labs_examples.arrays.labs;

import java.util.ArrayList;
import java.util.Collections;

/**
 *  ArrayLists
 *
 *      Please demonstrate how to create an ArrayList, populate an array list, access elements within an ArrayList.
 *      Also take a moment to explore the many methods that are available to you when you use an ArrayList. By simply
 *      typing the dot operator (".") after the ArrayList object that you create. You should see a menu pop up that
 *      shows a list of methods.
 *
 */
public class Exercise_07 {
    public static void main(String[] args) {

        ArrayList<String> shopping = new ArrayList<String>();

        shopping.add("Chicken");
        shopping.add("Sause");
        shopping.add("Bread");
        shopping.add("Tea");
        shopping.add("Cookie");
        shopping.add("Napkin");
        shopping.add("S&W500");
        shopping.add("Toothpaste");

        System.out.println("Initial list: " + shopping);
        System.out.println("Badass revolver: " + shopping.get(6));
        shopping.remove(6);
        System.out.println("Weapons are not allowed to common Russian citizens! Removing Smith & Wesson :(");
        System.out.println("Modified list: " + shopping);

        shopping.set(0, "Turkey");
        System.out.println("Tea is in the list: " + shopping.contains("Tea"));

        ArrayList<String> anotherShopping = new ArrayList<String>(shopping);
        shopping.clear();

        System.out.println("Another list: " + anotherShopping);
        System.out.println(anotherShopping.lastIndexOf("Napkin"));
        System.out.println(anotherShopping.size());
        Collections.sort(anotherShopping);
        System.out.println("Another list: " + anotherShopping);

        shopping.addAll(anotherShopping);
        System.out.println("Initial list: " + shopping);
    }
}
