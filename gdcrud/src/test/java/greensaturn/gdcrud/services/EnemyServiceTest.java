package greensaturn.gdcrud.services;

import greensaturn.gdcrud.model.Enemy;
import greensaturn.gdcrud.repositories.EnemyRepository;
import org.apache.coyote.BadRequestException;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentCaptor;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.assertj.core.api.AssertionsForClassTypes.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.*;

// Unit Test with Mockito
//@ExtendWith(MockitoExtension.class)
class EnemyServiceTest {
    @Mock
    private EnemyRepository enemyRepository;
    private EnemyService testService;
    @InjectMocks
    private EnemyService testServiceMock;
    private AutoCloseable autoCloseable;

    Integer testId = 17;
    String name = "zorro";

    @BeforeEach
    void setUp(){
        autoCloseable = MockitoAnnotations.openMocks(this);
        testService = new EnemyService(enemyRepository);
    }
    @AfterEach
    void tearDown() throws Exception{
        autoCloseable.close();

    }

    @Test
    void canGetAllEnemies() {
        // when
        testService.findAllEnemies();
        //then
        verify(enemyRepository).findAll();

    }

    @Test
    void canFindEnemyById() {
        testService.findEnemyById(testId);
        verify(enemyRepository).findById(testId);
    }

    @Test
    void canFindEnemyByName() {
        testService.findEnemyByName(name);
        verify(enemyRepository).findByName(name);
    }

    @Test
    void canAddEnemy() throws BadRequestException {
        // given
        Enemy testEnemy = new Enemy(testId,name,name,1,10,"a","b","s");
        // when
        testService.saveEnemy(testEnemy);
        //then
        // ArgumentCaptor sirve para asegurar que el parametro que que se mando al repositorio coincida con el que mandamos al servicio.
        ArgumentCaptor<Enemy> enemyArgumentCaptor = ArgumentCaptor.forClass(Enemy.class);
        verify(enemyRepository).save(enemyArgumentCaptor.capture());
        Enemy capturedEnemy = enemyArgumentCaptor.getValue();
        assertThat(capturedEnemy).isEqualTo(testEnemy);
    }
    @Test
    void addEnemyReturnName() throws BadRequestException {
        // given
        Enemy mockTestEnemy = new Enemy(testId,name,name,1,10,"a","b","s");
        // when
        when(enemyRepository.save(any(Enemy.class))).thenReturn(new Enemy(testId,name,name,1,10,"a","b","s"));
        //then
        Enemy mockedEnemy = testServiceMock.saveEnemy(mockTestEnemy);
        assertThat(mockedEnemy.getName()).isSameAs(mockTestEnemy.getName());
    }
    @Test
    void willThrowExceptionWhenNameRepeated() {
        // given
       /* Enemy testEnemy = new Enemy(testId,name,name,1,10,"a","b","s");


        given(enemyRepository.selectExistsName(anyString()))
                .willReturn(true);

        // when
        // then
        assertThatThrownBy(() -> testService.saveEnemy(testEnemy))
                .isInstanceOf(BadRequestException.class)
                .hasMessageContaining("An enemy with that name already exist.");

        verify(enemyRepository, never()).save(any());
*/
    }


    @Test
    @Disabled
    void canAddEnemyBatch() {
        //testService.saveEnemyBatch(testEnemy);
        //verify(enemyRepository).saveBatch(testEnemy);
    }

    @Test
    void deleteEnemy() {
        testService.deleteEnemy(testId);
        verify(enemyRepository).deleteById(testId);
    }
}