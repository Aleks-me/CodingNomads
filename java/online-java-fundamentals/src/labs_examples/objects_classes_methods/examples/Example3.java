package labs_examples.objects_classes_methods.examples;

// Add methods to Vehicle.
class Vehicle_4_3 {
    int passengers; // number of passengers
    int fuelcap;    // fuel capacity in gallons
    int mpg;        // fuel consumption in miles per gallon
    double speed;

    public int range() {
        return fuelcap * mpg;
    }

    public void accelerate(double speed){
        this.speed += speed;
    }
}

class AddMeth {
    public static void main(String[] args) {
        Vehicle_4_3 minivan = new Vehicle_4_3();
        Vehicle_4_3 sportscar = new Vehicle_4_3();

        minivan.passengers = 7;
        minivan.fuelcap = 16;
        minivan.mpg = 21;
        minivan.speed = 45;
        minivan.accelerate(20);

        //print speed()
        System.out.println("Minivan speed now is " + minivan.speed);

        sportscar.passengers = 2;
        sportscar.fuelcap = 14;
        sportscar.mpg = 12;

        System.out.println("Minivan can carry " + minivan.passengers + " for " + minivan.range());
        System.out.println("Sportscar can carry " + sportscar.passengers + " for " + sportscar.range());

    }
}