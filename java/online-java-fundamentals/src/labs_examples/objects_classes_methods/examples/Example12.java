package labs_examples.objects_classes_methods.examples;

// Add a constructor.

class Vehicle {
    int passengers; // number of passengers
    int fuelcap;    // fuel capacity in gallons
    int mpg;        // fuel consumption in miles per gallon

    // This is a constructor for Vehicle.
    Vehicle(int passengers, int fuelcap, int mpg) {
        this.passengers = passengers;
        this.fuelcap = fuelcap;
        this.mpg = mpg;
    }

    // Return the range.
    int range() {
        return mpg * fuelcap;
    }

    // Compute fuel needed for a given distance.
    double fuelNeeded(int miles) {
        return (double) miles / mpg;
    }
}

class VehConsDemo {
    public static void main(String[] args) {

        // construct complete vehicles
        Vehicle minivan = new Vehicle(7, 16, 21);
        Vehicle sportscar = new Vehicle(2, 14, 12);

        double gallons;

        gallons = minivan.fuelNeeded(minivan.range());

        System.out.println("To go " + minivan.range() + " miles minivan needs " +
                gallons + " gallons of fuel.");

        gallons = sportscar.fuelNeeded(minivan.range());

        System.out.println("To go " + minivan.range() + " miles sportscar needs " +
                gallons + " gallons of fuel.");

    }
}