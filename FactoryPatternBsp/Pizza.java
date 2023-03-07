public abstract class Pizza { 
    private int basisState; 
    public void prepare() { 
        System.out.println("Ihre Pizza wird gerade zubereitet."); 
    } 
    public void setState(int state) { 
        this.basisState = state; 
    } 
    public int getState() { 
        return basisState; 
    } 
    public abstract int getPrice(); 
    public abstract String getName();
    public abstract String getPizzeria();
} 

class BerlinCalzone extends Pizza { 

    @Override 
    public int getPrice() { 
        return 1400; 
    } 
    @Override
    public String getName() {
        return "Calzone";
    }
    @Override
    public String getPizzeria() {
        return "Berlin";
    }
} 

class BerlinSalami extends Pizza { 

    @Override 
    public int getPrice() { 
        return 2200; 
    } 
    @Override
    public String getName(){
        return "Salami";
    }
    @Override
    public String getPizzeria() {
        return "Berlin";
    }
} 

class BerlinHawaii extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    @Override
    public String getName() {
        return "Hawaii";
    }
    @Override
    public String getPizzeria() {
        return "Berlin";
    }
}

class BerlinQuattroStagioni extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    @Override
    public String getName() {
        return "QuattroStagioni";
    }
    @Override
    public String getPizzeria() {
        return "Berlin";
    }
}

class HamburgCalzone extends Pizza { 

    @Override 
    public int getPrice() { 
        return 1400; 
    } 
    @Override
    public String getName() {
        return "Calzone";
    }
    @Override
    public String getPizzeria() {
        return "Hamburg";
    }
}

class HamburgSalami extends Pizza { 

    @Override 
    public int getPrice() { 
        return 2200; 
    } 
    @Override
    public String getName() {
        return "Salami";
    }
    @Override
    public String getPizzeria() {
        return "Hamburg";
    }
}

class HamburgHawaii extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    @Override
    public String getName() {
        return "Hawaii";
    }
    @Override
    public String getPizzeria() {
        return "Hamburg";
    }
}

class HamburgQuattroStagioni extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    }
    @Override
    public String getName() {
        return "QuattroStagioni";
    }
    @Override
    public String getPizzeria() {
        return "Hamburg";
    }
}

class RostockCalzone extends Pizza { 

    @Override 
    public int getPrice() { 
        return 1400; 
    } 
    @Override
    public String getName() {
        return "Calzone";
    }
    @Override
    public String getPizzeria() {
        return "Rostock";
    }
}

class RostockSalami extends Pizza { 

    @Override 
    public int getPrice() { 
        return 2200; 
    } 
    @Override
    public String getName(){
        return "Salami";
    }
    @Override
    public String getPizzeria() {
        return "Rostock";
    }
}

class RostockHawaii extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    @Override
    public String getName() {
        return "Hawaii";
    }
    @Override
    public String getPizzeria() {
        return "Rostock";
    }
}

class RostockQuattroStagioni extends Pizza { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    @Override
    public String getName() {
        return "QuattroStagioni";
    }
    @Override
    public String getPizzeria() {
        return "Rostock";
    }
}
