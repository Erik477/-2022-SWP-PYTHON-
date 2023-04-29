public class Ticket{
    private TicketA mticket;

    public Ticket(TicketA mticket) {
        this.mticket = mticket;
        System.out.println("Printing " + mticket.type + " ticket for " + this.getPrice());
    }

    public double getPrice() {
       return mticket.getprice();
    }
}