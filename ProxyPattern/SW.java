package ProxyPattern;

public class SW implements InterfaceDrucker{
    
    @Override
    public void print(String FilePath,String Printer) throws Exception {
        System.out.print("Color Printing:");
        System.out.println(FilePath);
    }
}
