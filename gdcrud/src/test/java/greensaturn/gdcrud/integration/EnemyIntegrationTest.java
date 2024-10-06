package greensaturn.gdcrud.integration;

import com.fasterxml.jackson.databind.ObjectMapper;
import greensaturn.gdcrud.model.Enemy;
import greensaturn.gdcrud.repositories.EnemyRepository;
import org.junit.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
//import com.github.javafaker.Faker;

import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.ResultActions;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
@SpringBootTest
@TestPropertySource(
        locations = "classpath:application.properties"
)
@RunWith(SpringRunner.class)
@AutoConfigureMockMvc
@ExtendWith({ SpringExtension.class})
public class EnemyIntegrationTest {
// TODO test con mockito https://github.com/amigoscode/spring-boot-fullstack-professional/blob/13-testing/src/test/java/com/example/demo/integration/StudentIT.java
    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper = new ObjectMapper();

    @Autowired
    private EnemyRepository enemyRepository;

   // private final Faker faker = new Faker();
    @Test
    public void canRegisterNewEnemy() throws Exception {
        // given
        String name = String.format(
                "%s %s",
                "Seba",//faker.name().firstName(),
                "Pica "//faker.name().lastName()
        );

        Enemy enemy = new Enemy(1,"zorro","Un tierno zorro",1,10,"Nada","Nada","Nada");


        // when
        ResultActions resultActions = mockMvc
                .perform(post("/api/v1/enemy")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(this.objectMapper.writeValueAsString(enemy)));
        // then
        resultActions.andExpect(status().isOk());
        List<Enemy> enemies = enemyRepository.findAll();
        assertThat(enemies)
                .usingElementComparatorIgnoringFields("id")
                .contains(enemy);
    }
}
