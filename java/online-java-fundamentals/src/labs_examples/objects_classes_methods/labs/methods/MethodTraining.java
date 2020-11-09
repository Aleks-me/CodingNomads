package labs_examples.objects_classes_methods.labs.methods;

import java.util.ArrayList;
import java.util.Arrays;

public class MethodTraining {
    public static void main(String[] args) {

        System.out.println("Test by reference:");
        forTest obj = new forTest("green");
        System.out.println("Original color: " + obj.getColor());
        obj.changeColor("blue");
        System.out.println("New color: " + obj.getColor());
        System.out.println();
        System.out.println("Test by value:");
        int a = 1, b = 5;
        System.out.println("Original values: " + a + ", " + b);
        System.out.println("Pass by value: " + add(a, b));
        System.out.println("Original values untouched: " + a + ", " + b);
        System.out.println();
        System.out.println("Largest from 4:");
        System.out.println(largestFrom(2, -4, 16, -18));
        System.out.println();
        System.out.println("Overloaded largest from:");
        System.out.println(largestFrom(new int[]{-10, -5, 5, 10}));
        System.out.println();
        System.out.println("Calculate consonants:");
        System.out.println(consCount("string"));
        System.out.println();
        System.out.println("Some graphics:");
        printArt();
        System.out.println();
        System.out.println("Check Prime:");
        System.out.println(isPrime(5));
        System.out.println();
        System.out.println("Find max:");
        int[] anotherArray = new int[]{12, 3, 5, 14, 6 ,-20, -70, 100};
        System.out.println(minMaxFromArray(anotherArray));
        System.out.println();
        System.out.println("Ints that divizible:");
        ArrayList<Integer> ret = returner(10, 1, 2);
        System.out.println("Array: " + ret + ", size: " + ret.size());
        System.out.println();
        System.out.println("Reverse array:");
        int[] testArr = new int[]{1, 3, 5, 6, 8, 13, 29, 57, 70};
        System.out.println(Arrays.toString(reverser(testArr)));
    }

    static int add(int one, int two){
        return one + two;
    }

    static class forTest{
        String color;

        forTest(String color){
            this.color = color;
        }

        void changeColor(String col){
            color = col;
        }

        public String getColor() {
            return color;
        }
    }

    static int largestFrom(int a, int b, int c, int z){
        int max = 0;
        if(a > max) max = a;
        if(b > a) max = b;
        if(c > b) max = c;
        if(z > c) max = z;
        return max;
    }

    static int largestFrom(int[] arrInts){
        int max = 0;
        for(int i : arrInts){
            if(i > max) max = i;
        }
        return max;
    }

    static int consCount(String str){
        char[] vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};
        int counter = 0;
        int lenInput = str.length();
        for(char c : vowels){
            for(char l : str.toCharArray()){
                if (c == l) counter++;
            }
        }
        return lenInput - counter;
    }

    static void printArt(){
        System.out.println("**              **              **");
        System.out.println("  **          **  **          **  ");
        System.out.println("    **      **      **      **    ");
        System.out.println("      **  **          **  **      ");
        System.out.println("        **              **        ");
        System.out.println("      **  **          **  **      ");
        System.out.println("    **      **      **      **    ");
        System.out.println("  **          **  **          **  ");
        System.out.println("**              **              **");
    }

    static boolean isPrime(int num){
        boolean isPrime = false;
        for (int i = 2; i <= num / 2; ++i) {
            if (num % i == 0) {
                isPrime = true;
                break;
            }
        }
        return isPrime;
    }

    static ArrayList<Integer> minMaxFromArray(int[] iarr){
        ArrayList<Integer> temp = new ArrayList<>();
        int min = 0, max = 0;
        for(int v : iarr){
            if(v < min){
                min = v;
            } else if(v > max){
                max = v;
            }
        }
        temp.add(min);
        temp.add(max);
        return temp;
    }

    static int[] reverser(int[] nums){
        int temp;
        for(int i = 0; i < nums.length / 2; i++){
            temp = nums[i];
            nums[i] = nums[nums.length-(i+1)];
            nums[nums.length-(i+1)] = temp;
        }
        return nums;
    }

    static ArrayList<Integer> returner(int maxNum, int divisor1, int divisor2){
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i = 0; i < maxNum; i++) {
            if ((i % divisor1 == 0) && (i % divisor2 == 0)) {
                temp.add(i);
            }
        }
        return temp;
    }

}
