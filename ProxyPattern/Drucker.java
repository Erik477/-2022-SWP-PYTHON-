package ProxyPattern;

public class Drucker {
    private InterfaceDrucker drucker = new SW();
   
    public void print(String FilePath) throws Exception {
        drucker.print(FilePath);
    }

    public void switchDrucker(InterfaceDrucker andererdrucker) {
        this.drucker = andererdrucker;
    }
}