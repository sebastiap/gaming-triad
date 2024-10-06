package greensaturn.gdcrud.exception;

import org.springframework.http.HttpStatus;

import java.time.ZonedDateTime;

public class EnemyNotFoundException extends RuntimeException{

    public EnemyNotFoundException(String message) {
        super(message);
    }

    public EnemyNotFoundException(String message, Throwable cause) {
        super(message, cause);
    }

}
