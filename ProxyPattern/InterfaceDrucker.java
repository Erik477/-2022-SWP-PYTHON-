package ProxyPattern;

public interface InterfaceDrucker {
    // alle Methoden in Interfaces sind implizit public und abstract
  // man könnte auch schreiben: "public abstract void print();"
    void print(String FilePath) throws Exception;
}
