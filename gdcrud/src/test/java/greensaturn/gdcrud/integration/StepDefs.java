package greensaturn.gdcrud.integration;


import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.cucumber.spring.CucumberContextConfiguration;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;


public class StepDefs extends CucumberIntegrationTest {

    @When("^the client calls /version$")
    public void the_client_issues_GET_version() throws Throwable {
        //executeGet("http://localhost:8080/version");
    }
}
