package pull;

public class HereAndGoneDisp implements Observer{

    private WeatherData weatherData;
    
    public HereAndGoneDisp(WeatherData weatherData){
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    
    public void update(){

        System.out.println("I am Here");
    }
}
