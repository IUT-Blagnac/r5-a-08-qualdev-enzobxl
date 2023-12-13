package dojo;

import java.util.ArrayList;
import java.util.List;

public class Order {

    private String ordermessage;
    private String from;
    private String to;
    private List<String> cocktails = new ArrayList<>();

    public void declareOwner(String from) {
        this.from = from;
    }

    public void declareTarget(String to) {
        this.to = to;
    }

    public List<String> getCocktails() {
        return this.cocktails;
    }

    public void writeOrderMessage(String message) {
        this.ordermessage = "From " + this.from + " to " + this.to + ": " + message;
    }

    public String getOrderMessage() {
        return this.ordermessage;
    }
}
