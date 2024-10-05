package practice;

public class Personaje {
    public String getNombre() {
        return nombre;
    }

    public Integer getVida_min() {
        return vida_min;
    }

    public Integer getVida_max() {
        return vida_max;
    }

    private String nombre;
    private Integer vida_min;
    private Integer vida_max;
    public String presentarse (){
        return "Soy un personaje";
    }

    public Personaje(String nombre,Integer min,Integer max){
        this.nombre = nombre;
        this.vida_min = min;
        this.vida_max=max;
    }


}
