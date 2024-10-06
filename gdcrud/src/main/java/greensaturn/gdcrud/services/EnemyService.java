package greensaturn.gdcrud.services;

import greensaturn.gdcrud.model.Enemy;
import greensaturn.gdcrud.repositories.EnemyRepository;
import org.apache.coyote.BadRequestException;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;


@Service
public class EnemyService {
    private EnemyRepository enemyRepo;
    public EnemyService(EnemyRepository contRepo) {
        this.enemyRepo = contRepo;
    }
    public List<Enemy> findAllEnemies() {
        return enemyRepo.findAll();
    }
    public Optional<Enemy> findEnemyById(Integer id){
        return enemyRepo.findById(id);
    }
    public Optional<Enemy> findEnemyByName(String name){
        return enemyRepo.findByName(name);
    }

    public Boolean selectExistsName(String name){return enemyRepo.selectExistsName(name);};
    public Enemy saveEnemy(Enemy newEnemy) throws BadRequestException {
        Boolean enemyExist = enemyRepo.selectExistsName(newEnemy.getName());
        if (enemyExist) {
            throw new BadRequestException("An enemy with that name already exist.");
        }
        return enemyRepo.save(newEnemy);
    }
    public Enemy saveEnemyBatch(Enemy newEnemy) {
        return enemyRepo.saveBatch(newEnemy);
    }
    public void deleteEnemy(Integer id) {  enemyRepo.deleteById(id);}



}
