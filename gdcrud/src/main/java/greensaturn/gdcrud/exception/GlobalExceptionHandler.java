package greensaturn.gdcrud.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Date;

@ControllerAdvice
public class GlobalExceptionHandler {
// ControllerAdvice es un annotation que captura las excepciones globalmente
    // para todos los componentes

    @ExceptionHandler(EnemyBadRequestException.class)
    // Aplica este metodo a todas las excepciones de clase EnemyBadRequest
    public ResponseEntity<?> handleEnemyBadRequestException(EnemyNotFoundException ex ){
        // 1. Creo una respuesta con los detalles de la excepcion
        HttpStatus badRequestCode = HttpStatus.NOT_FOUND;

        // Reemplazadas con atajo CTRL  + ALT + V
        ZonedDateTime timestamp = ZonedDateTime.now(ZoneId.of("Z"));
        ApiException payload = new ApiException(ex.getMessage(),
                badRequestCode,
                timestamp);
        // 2. Retorno una entidad de respuesta
                return new ResponseEntity<>(payload , badRequestCode);

    }
    @ExceptionHandler(EnemyNotFoundException.class)
    // Aplica este metodo a todas las excepciones de clase EnemyNotFound
    public ResponseEntity<?> handleEnemyNotFoundException(EnemyNotFoundException ex){
        ZonedDateTime timestamp = ZonedDateTime.now(ZoneId.of("Z"));
        HttpStatus notFoundCode = HttpStatus.NOT_FOUND;
        ApiException payload = new ApiException(
                ex.getMessage(),
                notFoundCode,
                ZonedDateTime.now(ZoneId.of("Z")));

                return new ResponseEntity<>(payload , notFoundCode);

    }
}
