# GDcrud

## About this project
 Una API en springboot para realizar operaciones sobre una base de datos para juegos.


## Testing 

* Unit Testing with Junit.
* Integration test by REST Assured (Pending).
* Service Testing and Mocking with Mockito.

## Error Fixes

### Sequence for Enemy Model
Para evitar un error con la secuencia la tuve que crear de esta manera.
~~~
CREATE SEQUENCE SEQ_ENEMY INCREMENT BY 50 START WITH 1 OWNED BY ENEMY.ID;
~~~
### La secuencia toma el numero al iniciar el programa
No importa si dropeo o reinicio la sequencia, Spring Boot seguira usando el numero que ya le pasamos.



