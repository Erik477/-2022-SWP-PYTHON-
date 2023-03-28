package ProxyPattern;

public class Client {
    public static void main (String[] args)
    {
        InterfaceDrucker printer = new Drucker();
        try
        {
            printer.print("Laborbericht.png","SW");
            printer.print("Laborbericht.png","Color");
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
