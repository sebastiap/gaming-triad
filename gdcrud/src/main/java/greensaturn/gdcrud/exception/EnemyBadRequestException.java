package greensaturn.gdcrud.exception;

import org.springframework.http.HttpStatus;

import java.time.ZonedDateTime;

public class EnemyBadRequestException extends RuntimeException{


    public EnemyBadRequestException(String message) {
        super(message);
    }

    public EnemyBadRequestException(String message, Throwable cause) {
        super(message, cause);
    }

}
