import java.util.Scanner;

public class Client { 
    public static void main(String[] args) { 
        Scanner Order = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Wo möchten Sie Ihre Pizza bestellen? Berlin, Hamburg oder Rostock?");
        String Pizzeria = Order.nextLine();  // Read user input
        System.out.println("Welche Pizza möchten Sie bestellen? Calzone, Salami, Hawaii oder QuattroStagioni?");
        String PizzaTyp = Order.nextLine();  // Read user input
        Order.close();
        Pizza product = null;

        switch(Pizzeria) {
            case "Berlin":
                BerlinPizzeria berPiz = new BerlinPizzeria();
                product = berPiz.createProduct(PizzaTyp);
                break;
            case "Hamburg":
                HamburgPizzeria habPiz = new HamburgPizzeria();
                product = habPiz.createProduct(PizzaTyp);
                break;
            case "Rostock":
                RostockPizzeria rosPiz = new RostockPizzeria();
                product = rosPiz.createProduct(PizzaTyp);
                break;
            default:
                System.out.println("Falsche Eingabe!");
        }
        System.out.println("Die Pizza "+ product.getName()+ " von der Pizzeria in "+ product.getPizzeria()+ " kostet " +product.getPrice() + " Euro."); 
    } 
}
