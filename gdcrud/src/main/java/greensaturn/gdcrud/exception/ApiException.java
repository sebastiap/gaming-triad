package greensaturn.gdcrud.exception;

import org.springframework.http.HttpStatus;

import java.time.ZonedDateTime;

public class ApiException extends RuntimeException{
// Clase que representa la entidad de las excepciones
    private final String message;
    private final HttpStatus httpStatus;
    private ZonedDateTime timestamp;

    public ApiException(String message, HttpStatus httpStatus , ZonedDateTime timestamp)
    {
        this.message = message;
        this.httpStatus = httpStatus;
        this.timestamp = timestamp;
    }
// Generados con ALT + INSERT
    @Override
    public String getMessage() {
        return message;
    }

    public HttpStatus getHttpStatus() {
        return httpStatus;
    }

    public ZonedDateTime getTimestamp() {
        return timestamp;
    }

}
