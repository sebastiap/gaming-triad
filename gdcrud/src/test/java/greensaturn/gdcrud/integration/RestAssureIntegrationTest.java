package greensaturn.gdcrud.integration;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.annotations.Test;

@Test
public class RestAssureIntegrationTest {

    public void RAtest() {

        // TODO -- Ver porque da el puto error
        // Comparar con el de la pc del trabajo
        Response response = RestAssured.get("http://localhost:8080/api/v1/enemy/version");
        System.out.println(response.getStatusCode());
        System.out.println(response.getTime());
    ;
    }
}
