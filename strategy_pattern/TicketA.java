public abstract class TicketA {
    private float price;
    private float taxrate;
    protected String type;

    public TicketA(float price, float taxrate) {
        this.price = price;
        this.taxrate = taxrate;
    }

    public float getprice() {
        return this.price * (1+this.taxrate/100);
    }
}