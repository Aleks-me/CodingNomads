package labs_examples.conditions_loops.examples;

// Show square roots of 1 to 99 and the rounding error.
class SqrRoot {
    public static void main(String[] args) {
        double num, sqroot, rerr;

        for(num = 1.0; num < 100.0; num++) {
            sqroot = Math.sqrt(num);
            System.out.println("Square root of " + num +
                    " is " + sqroot);

            // compute rounding error
            rerr = num - (sqroot * sqroot);
            System.out.println("Rounding error is " + rerr);
            System.out.println();
        }
    }
}