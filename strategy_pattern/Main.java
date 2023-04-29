/*
 * Use strategy pattern to solve the following problem.
Baltimore Orioles Stadium Ticket Office invites software firms to bid for a project. They want to have a
class library (with classes and interface) to calculate ticket sale price. Here are the rules for ticket sale
at Stadium:
- Ticket sale price consist of two parts: ticket price and sale tax.
- Ticket price varies between children (age under 16 - $10 ), adults ($15) and seniors
(age 65+ - $12).
Baltimore Orioles Stadium Ticket Office will award the project to the design that allows users to add
more ticket categories and tax rate calculation changes easily.
 * 
 */

public class Main {
    public static void main(String [] args){
        Ticket t1 = new Ticket(new ChildCalcLogic(10));
        Ticket t2 = new Ticket(new AdultCalcLogic(20));
        Ticket t3 = new Ticket(new SeniourCalcLogic(10));
        Ticket t4 = new Ticket(new StudentCalcLogic(5));
    }
}
