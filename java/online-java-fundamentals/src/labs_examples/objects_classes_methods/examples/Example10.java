package labs_examples.objects_classes_methods.examples;//package main.java.chapter4;

// A simple constructor.

class MyClass_4_10 {
    final float pi = 3.14195678f;
    int y = 10;
    int z = 2;
}

class ConsDemo {
    public static void main(String[] args) {
        MyClass_4_10 t1 = new MyClass_4_10();
        MyClass_4_10 t2 = new MyClass_4_10();

        float result = t1.z + t1.y + t2.pi;
        System.out.println("Sum is " + result);
    }
}