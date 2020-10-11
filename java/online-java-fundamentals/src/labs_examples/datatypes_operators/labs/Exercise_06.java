package labs_examples.datatypes_operators.labs;

/**
 * Fundamentals Exercise 4: Volume and Surface Area
 *
 *      Write the necessary code to calculate the volume and surface area of a cylinder
 *      with a radius of 3.14 and a height of 5. Print out the result.
 *
 */

public class Exercise_06 {

    public static void main(String[] args) {

        // write code here
        float pi = 3.14f;
        float radius = pi;
        int height = 5;

        float volume = (float) (pi*((radius*2)*(radius*2))/4)*height;
        float surfArea = (float) (pi*((radius*2)*(radius*2))/2)+pi*(radius*2)*height;

        System.out.println("Cylinder volume is: " + volume + ", cylinder surface area is: " + surfArea);
    }
}