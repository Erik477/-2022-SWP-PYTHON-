public abstract class Pizzeria { 

    public Pizza createProduct(String PizzaTyp) { 
        //holt konkretes Product, weiß nicht welches. 
        Pizza product = factoryMethod(PizzaTyp); 

        //allgemeiner Productherstellungscode 
        product.setState(23); 
        product.prepare(); 
        return product; 
    } 

    protected abstract Pizza factoryMethod(String PizzaTyp); 
} 

class BerlinPizzeria extends Pizzeria { 

    protected Pizza factoryMethod(String PizzaTyp) { 
        switch (PizzaTyp) {
            case "Calzone":
                BerlinCalzone berCal = new BerlinCalzone();
                return berCal;
            case "Salami":
                BerlinSalami berSal = new BerlinSalami();
                return berSal;
            case "Hawaii":
                BerlinHawaii berHaw = new BerlinHawaii();
                return berHaw;
            case "QuattroStagioni":
                BerlinQuattroStagioni berQuattro = new BerlinQuattroStagioni();
                return berQuattro;
            default:
                return null;
        }
    } 
} 

class HamburgPizzeria extends Pizzeria { 

    protected Pizza factoryMethod(String PizzaTyp) { 
        switch (PizzaTyp) {
            case "Calzone":
                HamburgCalzone habCal = new HamburgCalzone();
                return habCal;
            case "Salami":
                HamburgSalami habSal = new HamburgSalami();
                return habSal;
            case "Hawaii":
                HamburgHawaii habHaw = new HamburgHawaii();
                return habHaw;
            case "QuattroStagioni":
                HamburgQuattroStagioni habQuattro = new HamburgQuattroStagioni();
                return habQuattro;
            default:
                return null;
        }
    } 
}

class RostockPizzeria extends Pizzeria { 

    protected Pizza factoryMethod(String PizzaTyp) { 
        switch (PizzaTyp) {
            case "Calzone":
                RostockCalzone rosCal = new RostockCalzone();
                return rosCal;
            case "Salami":
                RostockSalami rosSal = new RostockSalami();
                return rosSal;
            case "Hawaii":
                RostockHawaii rosHaw = new RostockHawaii();
                return rosHaw;
            case "QuattroStagioni":
                RostockQuattroStagioni rosQuattro = new RostockQuattroStagioni();
                return rosQuattro;
            default:
                return null;
        }
    } 
}