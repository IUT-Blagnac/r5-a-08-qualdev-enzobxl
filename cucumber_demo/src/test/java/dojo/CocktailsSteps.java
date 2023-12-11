package dojo;

import cucumber.api.java.en.And;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

import java.util.List;

import static org.junit.Assert.assertEquals;

public class CocktailsSteps {
    private Order order;

    @Given("{string} who wants to buy a drink")
    public void fromWhoWantsToBuyADrink(String from) {
        order = new Order();
        order.declareOwner(from);
    }

    @When("an order is declared for {string}")
    public void anOrderIsDeclaredForTo(String to) {
        order.declareTarget(to);
    }

    @And("a message saying {string} is added")
    public void aMessageSayingIsAdded(String message) {
        order.writeOrderMessage(message);
    }

    @Then("there is {int} cocktails in the order")
    public void thereIsNbCocktailsCocktailsInTheOrder(int nbCocktails) {
        List<String> cocktails = order.getCocktails();
        assertEquals(nbCocktails, cocktails.size());
    }

    @Then("the ticket must say {string}")
    public void theTicketMustSay(String message) {
        assertEquals(message, order.getOrderMessage());
    }
}
