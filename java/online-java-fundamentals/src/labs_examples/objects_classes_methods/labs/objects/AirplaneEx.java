package labs_examples.objects_classes_methods.labs.objects;

public class AirplaneEx {
    public static void main(String[] args) {

        InnerSpace salon = new InnerSpace(220,1,
                true, false);
        Turbine turbo = new Turbine(2, 200);
        Crew crew = new Crew(2, 4);
        CargoHold forCargo = new CargoHold(21200);
        FlightParameters flightData = new FlightParameters();
        Airplane Boeing = new Airplane(30000, 100, salon, turbo, crew, forCargo, flightData);

        System.out.println(salon.toString());
        System.out.println(turbo.toString());
        System.out.println(crew.toString());
        System.out.println(forCargo.toString());
        System.out.println(flightData.toString());
        System.out.println(Boeing.WhatDistLeft(2000));
        System.out.println(Boeing.WhatDistLeft(6000));
    }
}

class Airplane{
    public double fuelCap;
    public int fuelLeftPct;
    InnerSpace InSpace;
    Turbine engine;
    Crew pilots;
    CargoHold thingsSpace;
    FlightParameters flight;

    public Airplane(double fuelCap, int fuelLeftPct, InnerSpace inSpace,
                    Turbine engine, Crew pilots, CargoHold thingsSpace, FlightParameters flight) {
        this.fuelCap = fuelCap;
        this.fuelLeftPct = fuelLeftPct;
        InSpace = inSpace;
        this.engine = engine;
        this.pilots = pilots;
        this.thingsSpace = thingsSpace;
        this.flight = flight;
    }

    String WhatDistLeft(int distPass) {
        if (flight.flightDist - distPass < 0) {
            return "Out of Fuel!";
        } else {
            return "Distance left " + (flight.flightDist - distPass);
        }
    }

    @Override
    public String toString() {
        return "Airplane{" +
                "fuelCap=" + fuelCap +
                ", fuelLeftPct=" + fuelLeftPct +
                ", InSpace=" + InSpace +
                ", engine=" + engine +
                ", pilots=" + pilots +
                ", thingsSpace=" + thingsSpace +
                '}';
    }
}

class InnerSpace{
    int seatsAmount;
    int numPassBetweenRows;
    boolean haveBusinessClass;
    boolean isCargo;

    public InnerSpace(int seatsAmount, int numPassagesBetweenRows, boolean haveBusinessClass, boolean isCargo) {
        this.seatsAmount = seatsAmount;
        this.numPassBetweenRows = numPassagesBetweenRows;
        this.haveBusinessClass = haveBusinessClass;
        this.isCargo = isCargo;
    }

    @Override
    public String toString() {
        return "InnerSpace{" +
                "seatsAmount=" + seatsAmount +
                ", numPassagesBetweenRows=" + numPassBetweenRows +
                ", haveBusinessClass=" + haveBusinessClass +
                ", isCargo=" + isCargo +
                '}';
    }
}

class Turbine{
    int turbineAmount;
    int turbineHp;

    public Turbine(int turbineAmount, int turbineHp){
        this.turbineAmount = turbineAmount;
        this.turbineHp = turbineHp;
    }

    @Override
    public String toString(){
        return "Turbine{" +
                "number of engines= " + turbineAmount +
                ", engine HP=" + turbineHp + "}";
    }
}

class Crew{
    int numPilots;
    int numStewardess;

    public Crew(int numPilots, int numStewardess) {
        this.numPilots = numPilots;
        this.numStewardess = numStewardess;
    }

    @Override
    public String toString() {
        return "Pilots{" +
                "numPilots=" + numPilots +
                ", numStewardess=" + numStewardess +
                '}';
    }
}

class CargoHold{
    float cargoCapacity;

    public CargoHold(float cargoVolume) {
        this.cargoCapacity = cargoVolume;
    }

    @Override
    public String toString() {
        return "CargoHold{" +
                "cargoVolume=" + cargoCapacity +
                '}';
    }
}

class FlightParameters{
    int maxFlightHeight = 11200;
    int maxSpeed = 890;
    int flightDist = 5000;
    int fuelPerHour = 3200;

    public FlightParameters() {
    }

    public FlightParameters(int maxFlightHeight, int maxSpeed, int flightDist, int fuelPerHour) {
        this.maxFlightHeight = maxFlightHeight;
        this.maxSpeed = maxSpeed;
        this.flightDist = flightDist;
        this.fuelPerHour = fuelPerHour;
    }

    @Override
    public String toString() {
        return "FlightParameters{" +
                "maxFlightHeight=" + maxFlightHeight +
                ", maxSpeed=" + maxSpeed +
                ", flightDist=" + flightDist +
                ", fuelPerHour=" + fuelPerHour +
                '}';
    }
}