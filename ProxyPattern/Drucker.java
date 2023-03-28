package ProxyPattern;

public class Drucker implements InterfaceDrucker {
    private InterfaceDrucker drucker;
    
    public Drucker() {
        drucker = new SW();
    }
    
    @Override
    public void print(String FilePath,String Printer) throws Exception {
        if (Printer == "SW") {
            drucker = new SW();
        } else {
            drucker = new Color();
        }
        drucker.print(FilePath,Printer);
    }
}