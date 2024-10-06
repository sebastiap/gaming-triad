package greensaturn.gdcrud.repositories;

import greensaturn.gdcrud.model.Enemy;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public interface EnemyRepository extends JpaRepository<Enemy,Integer> {

    public Optional<Enemy> findByName(String Name);

    public Optional<Enemy> findById(Integer id);
    public default Enemy saveBatch(Enemy enemy){
        List<Enemy> enemyBatch = new ArrayList<>();
        for (int i = 1; i < 21; i++) {
            Enemy auxEnemy = new Enemy(i,enemy.getName()+i,enemy.getDescription(),0,i,enemy.getAbilities(),enemy.getAttacks(),enemy.getLoot());
            enemyBatch.add(auxEnemy);
        }
        saveAll(enemyBatch);
        return enemy;
    };

    @Query("" +
            "SELECT CASE WHEN COUNT(s) > 0 THEN " +
            "TRUE ELSE FALSE END " +
            "FROM Enemy s " +
            "WHERE s.name = ?1"
    )
    public Boolean selectExistsName(String name);

}
