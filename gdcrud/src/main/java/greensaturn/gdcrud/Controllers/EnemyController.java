package greensaturn.gdcrud.Controllers;


import greensaturn.gdcrud.exception.EnemyBadRequestException;
import greensaturn.gdcrud.exception.EnemyNotFoundException;
import greensaturn.gdcrud.model.Enemy;
import greensaturn.gdcrud.services.EnemyService;
import org.apache.coyote.BadRequestException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@CrossOrigin
@RequestMapping("/api/v1/enemy")
public class EnemyController {
    record enemyRequest(
            Integer id,
            String name,
            String description,
            Integer min_life,
            Integer max_life,
            String abilities,
            String attacks,
            String loot
    ){

    }

    @GetMapping("/version")
    public String getVersion() {
        return "1.0";
    }

    private Enemy setEnemy(Enemy enemy, EnemyController.enemyRequest request){
        enemy.setId(request.id);
        enemy.setName(request.name);
        enemy.setDescription(request.description);
        enemy.setMin_life(request.min_life);
        enemy.setMax_life(request.max_life);
        enemy.setAbilities(request.abilities);
        enemy.setAttacks(request.attacks);
        enemy.setLoot(request.loot);
        return enemy;
    }

    @Autowired
    EnemyService enemyService;

    @GetMapping("/")
    private List<Enemy> getAll(){
        List<Enemy> result = enemyService.findAllEnemies();
        return result;
    }
    @GetMapping("/id/{id}")
    private Optional<Enemy> getById(@PathVariable Integer id){

        if (id == 0){
            throw new EnemyBadRequestException("The Request has invalid parameters");
        }

        Optional<Enemy> result = enemyService.findEnemyById(id);
        if (result.isEmpty()){
            throw new EnemyNotFoundException("Enemy can not be found on the database");
        }
        return result;
    };
    @GetMapping("/name/{name}")
    private ResponseEntity<Enemy> getByName( @PathVariable String name){
        Boolean exists = enemyService.selectExistsName(name);
        if (!exists) {
            throw new EnemyNotFoundException("Enemy can not be found on the database");
        }
        else{
            Optional<Enemy> result = enemyService.findEnemyByName(name);
            if (result.isEmpty()){
                throw new EnemyNotFoundException("Enemy can not be found on the database");
            }
            return new ResponseEntity<Enemy>(result.get(),HttpStatus.OK); }

    };
    @GetMapping("/confirm/{name}")
    private ResponseEntity<Boolean> confirmByName( @PathVariable String name){
        Boolean exists = enemyService.selectExistsName(name);
        return new ResponseEntity<Boolean>(enemyService.selectExistsName(name), HttpStatus.ACCEPTED);

    };
    @PostMapping("/")
    private ResponseEntity<Enemy> createNewEnemy (@RequestBody EnemyController.enemyRequest request){
        Enemy newEnemy = new Enemy();
        setEnemy(newEnemy,request);
        try {
            return new ResponseEntity<Enemy>(enemyService.saveEnemy(newEnemy), HttpStatus.CREATED);
            // TODO ver si este try catch hace falta
        } catch (BadRequestException e) {
            throw new RuntimeException(e);
        }
    }

    @PostMapping("/batch")
    private ResponseEntity<Enemy> createNewEnemyBatch (@RequestBody EnemyController.enemyRequest request){
        Enemy newEnemy = new Enemy();
        setEnemy(newEnemy,request);
        return new ResponseEntity<Enemy>(enemyService.saveEnemyBatch(newEnemy), HttpStatus.CREATED);
    }
@DeleteMapping("/id/{id}")
    private ResponseEntity<Enemy> deleteEnemybyId(@ PathVariable Integer id) {
          enemyService.deleteEnemy(id);
    ResponseEntity response = new ResponseEntity<>(HttpStatus.OK);
    return response;
    }
}
