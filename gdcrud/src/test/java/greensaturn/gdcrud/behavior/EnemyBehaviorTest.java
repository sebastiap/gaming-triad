package greensaturn.gdcrud.behavior;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import org.junit.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.Assert.*;
@SpringBootTest
public class EnemyBehaviorTest {
    @Given("I have {int} cukes in my belly")
    public void i_have_n_cukes_in_my_belly(int cukes) {
        System.out.format("Cukes: %n\n", cukes);
    }
    @Then("the result should be {int}")
    @Test
    public void the_result_should_be(int expectedResult) {
        assertEquals(expectedResult, expectedResult);
    }
}
