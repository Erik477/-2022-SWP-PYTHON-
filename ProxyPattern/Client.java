package ProxyPattern;

public class Client {
    public static void main (String[] args)
    {
        Drucker printer = new Drucker();
        try
        {
            printer.print("Laborbericht.png");
            printer.switchDrucker(new Color());
            printer.print("Laborbericht.png");
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
