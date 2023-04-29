package ProxyPattern;

public class SW implements InterfaceDrucker{
    
    @Override
    public void print(String FilePath) throws Exception {
        System.out.print("SchwarzWeiß Printing:");
        System.out.println(FilePath);
    }
}
