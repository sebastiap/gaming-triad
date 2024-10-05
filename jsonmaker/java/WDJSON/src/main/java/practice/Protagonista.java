package practice;

// extends indica que heredo de Father
public class Protagonista extends Personaje {
    //private String nombre;
    private String apellido;

    public Protagonista(String nombre,Integer min,Integer max,String Apellido){
        // super asigna la informacion heredada
        super(nombre,min,max);
        this.apellido = Apellido;
    }
    // Esto es polimorfismo
    // Sobreescribo el comportamiento de presentarse con un comportamiento propio
    @Override
    public String presentarse (){
        return "Soy un el protagonista,"  + this.getNombre() + " " +  this.apellido;
    }
}
