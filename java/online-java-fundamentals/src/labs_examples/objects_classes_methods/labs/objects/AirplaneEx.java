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
        turbo.setTurbineAmount(4);
        System.out.println(turbo.toString());
    }
}

class Airplane{
    private double fuelCap;
    private int fuelLeftPct;
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
        if (flight.getFlightDist() - distPass < 0) {
            return "Out of Fuel!";
        } else {
            return "Distance left " + (flight.getFlightDist() - distPass);
        }
    }

    public double getFuelCap() {
        return fuelCap;
    }

    public void setFuelCap(double fuelCap) {
        this.fuelCap = fuelCap;
    }

    public int getFuelLeftPct() {
        return fuelLeftPct;
    }

    public void setFuelLeftPct(int fuelLeftPct) {
        this.fuelLeftPct = fuelLeftPct;
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
    private int seatsAmount;
    private int numPassBetweenRows;
    private boolean haveBusinessClass;
    private boolean isCargo;

    public InnerSpace(int seatsAmount, int numPassagesBetweenRows, boolean haveBusinessClass, boolean isCargo) {
        this.seatsAmount = seatsAmount;
        this.numPassBetweenRows = numPassagesBetweenRows;
        this.haveBusinessClass = haveBusinessClass;
        this.isCargo = isCargo;
    }

    public int getSeatsAmount() {
        return seatsAmount;
    }

    public void setSeatsAmount(int seatsAmount) {
        this.seatsAmount = seatsAmount;
    }

    public int getNumPassBetweenRows() {
        return numPassBetweenRows;
    }

    public void setNumPassBetweenRows(int numPassBetweenRows) {
        this.numPassBetweenRows = numPassBetweenRows;
    }

    public boolean isHaveBusinessClass() {
        return haveBusinessClass;
    }

    public void setHaveBusinessClass(boolean haveBusinessClass) {
        this.haveBusinessClass = haveBusinessClass;
    }

    public boolean isCargo() {
        return isCargo;
    }

    public void setCargo(boolean cargo) {
        isCargo = cargo;
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
    private int turbineAmount;
    private int turbineHp;

    public Turbine(int turbineAmount, int turbineHp){
        this.turbineAmount = turbineAmount;
        this.turbineHp = turbineHp;
    }

    public int getTurbineAmount() {
        return turbineAmount;
    }

    public void setTurbineAmount(int turbineAmount) {
        this.turbineAmount = turbineAmount;
    }

    public int getTurbineHp() {
        return turbineHp;
    }

    public void setTurbineHp(int turbineHp) {
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
    private int numPilots;
    private int numStewardess;

    public Crew(int numPilots, int numStewardess) {
        this.numPilots = numPilots;
        this.numStewardess = numStewardess;
    }

    public int getNumPilots() {
        return numPilots;
    }

    public void setNumPilots(int numPilots) {
        this.numPilots = numPilots;
    }

    public int getNumStewardess() {
        return numStewardess;
    }

    public void setNumStewardess(int numStewardess) {
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
    private float cargoCapacity;

    public CargoHold(float cargoVolume) {
        this.cargoCapacity = cargoVolume;
    }

    public float getCargoCapacity() {
        return cargoCapacity;
    }

    public void setCargoCapacity(float cargoCapacity) {
        this.cargoCapacity = cargoCapacity;
    }

    @Override
    public String toString() {
        return "CargoHold{" +
                "cargoVolume=" + cargoCapacity +
                '}';
    }
}

class FlightParameters{
    private int maxFlightHeight = 11200;
    private int maxSpeed = 890;
    private int flightDist = 5000;
    private int fuelPerHour = 3200;

    public FlightParameters() {
    }

    public FlightParameters(int maxFlightHeight, int maxSpeed, int flightDist, int fuelPerHour) {
        this.maxFlightHeight = maxFlightHeight;
        this.maxSpeed = maxSpeed;
        this.flightDist = flightDist;
        this.fuelPerHour = fuelPerHour;
    }

    public int getMaxFlightHeight() {
        return maxFlightHeight;
    }

    public void setMaxFlightHeight(int maxFlightHeight) {
        this.maxFlightHeight = maxFlightHeight;
    }

    public int getMaxSpeed() {
        return maxSpeed;
    }

    public void setMaxSpeed(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public int getFlightDist() {
        return flightDist;
    }

    public void setFlightDist(int flightDist) {
        this.flightDist = flightDist;
    }

    public int getFuelPerHour() {
        return fuelPerHour;
    }

    public void setFuelPerHour(int fuelPerHour) {
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