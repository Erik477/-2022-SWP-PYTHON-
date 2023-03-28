package Observer;

import java.util.Observable;


class Zentrale extends Observable {
    
    public Zentrale(){
        this.addObserver(new Bildschirm());
        this.addObserver(new Farbsignale());
        tell("laber, laber...");
    }
    
    public void tell(String info){
        if(countObservers()>0){
            setChanged();
            notifyObservers(info);
        }
    }
}