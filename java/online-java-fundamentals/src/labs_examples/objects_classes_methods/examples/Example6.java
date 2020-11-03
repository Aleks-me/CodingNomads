package labs_examples.objects_classes_methods.examples;

class ChkNum {
    // return true if x is even
    boolean isEven(int x) {
        return((x%2) == 0);
    }
}

class ParamDemo {
    public static void main(String[] args) {
        ChkNum e = new ChkNum();

        if(e.isEven(10)) {
            System.out.println("10 is even.");
        }

        if(e.isEven(9)) {
            System.out.println("9 is even.");
        }

        if(e.isEven(8))
            System.out.println("8 is even.");

    }
}