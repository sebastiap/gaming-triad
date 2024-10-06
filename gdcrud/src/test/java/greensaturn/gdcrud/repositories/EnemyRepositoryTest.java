package greensaturn.gdcrud.repositories;

import greensaturn.gdcrud.model.Enemy;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;


// UNIT TEST

@DataJpaTest
class EnemyRepositoryTest {

    @Autowired
    private EnemyRepository enemyRepoTest;

    @Test
    void itShouldCheckFindByName() {
        //given
        String enemyName = "zorro";
        Enemy enemigoZorro = new Enemy(1,"zorro","Un tierno zorro",1,10,"Nada","Nada","Nada");
        enemyRepoTest.save(enemigoZorro);
        //when
        Boolean exists = enemyRepoTest.findByName(enemyName).isPresent();
        //then
        assertThat(exists).isTrue();
    }

    @Test
    void itShouldFindById() {
        Enemy enemigoZorro = new Enemy(1,"zorro","Un tierno zorro",1,10,"Nada","Nada","Nada");
        enemyRepoTest.save(enemigoZorro);
        Boolean exists = enemyRepoTest.findById(1).isPresent();
        assertThat(exists).isTrue();
    }
    @Test
    void itShouldNotFindById() {
        Enemy enemigoZorro = new Enemy(1,"zorro","Un tierno zorro",1,10,"Nada","Nada","Nada");
        enemyRepoTest.save(enemigoZorro);
        Boolean exists = enemyRepoTest.findById(2).isPresent();
        assertThat(exists).isFalse();
    }
    @Test
    void itShouldDelete() {
        Enemy enemigoZorra = new Enemy(2,"zorra","Un tierno zorro",1,10,"Nada","Nada","Nada");
        enemyRepoTest.save(enemigoZorra);
        // TODO ver que onda este test
        //Boolean existed = enemyRepoTest.findById(2).isPresent();
        Boolean existed = enemyRepoTest.selectExistsName("zorra");
        enemyRepoTest.deleteById(2);
        //Boolean exists  = enemyRepoTest.selectExistsName("zorra");
        Boolean exists = enemyRepoTest.findById(2).isPresent();
        assertThat(existed).isTrue();
        assertThat(exists).isFalse();
    }

    @Test
    @Disabled
    void saveBatch() {
    }

}