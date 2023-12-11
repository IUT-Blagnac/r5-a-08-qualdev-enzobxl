package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class StepDefinitions {

    @Given("an example scenario")
    public void anExampleScenario() {
    }

    @When("all step definitions are implemented")
    public void allStepDefinitionsAreImplemented() {
    }

    @Then("the scenario passes")
    public void theScenarioPasses() {
    }

    @Given("today is Friday")
    public void todayIsFriday() {
    }

    @When("I ask whether it's Friday yet")
    public void iAskWhetherItSFridayYet() {
    }

    @Then("I should be told {string}")
    public void iShouldBeTold(String string) {
        assertEquals("TGIF", string);
    }

}