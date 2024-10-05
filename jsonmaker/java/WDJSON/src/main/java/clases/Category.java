package clases;

import org.json.simple.JSONObject;

import java.io.File;
import java.util.stream.Stream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class Category {
    // Recibe un nombre de categoria y permite ingresar un listado de items en esa categoria
    // Tambien se puede generar a partir de grupos predeterminados
    public Scanner prompt = new Scanner(System.in);


    public ArrayList<String> readAttributteFile(){
        ArrayList<String> att_list = new ArrayList<String>();
        System.out.println("Write the name of the category you want to create:");
        Stream fileStream = null;
        try {
            String filePath = new File("").getAbsolutePath();
            filePath = filePath.concat("/java/WDJSON/public/");
            fileStream = Files.lines(Paths.get(filePath + "attributes.txt"));

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        fileStream.sorted()
                .forEach(s ->att_list.add(s.toString()));
    return att_list;
}
    public String nameCategory (){
        String userInput = "Valor";
        System.out.println("Write the name of the category you want to create:");
        userInput = this.prompt.nextLine();
        return userInput;
    }

    public Map addAttributes(Integer count,Integer type){
        Map<String, String> data = new HashMap<>();
        switch (type) {
            case 1:
                data.put("ID", "" + count);
                data.put("Vida_minima", "100");
                data.put("Vida_maxima", "300");
                data.put("costo_unitario", "50");
                data.put("Loot", "100");
                break;
            case 2:
                data.put("Escala", "1");
                data.put("Max", "10");
                data.put("costo_unitario", "50");
                data.put("contrario", "Calor");
                break;
            case 3:
                data.put("Armadura", "1");
                data.put("Resistencia", "10");
                data.put("costo_basico", "50");
                break;
            default:
                data.put("ID", "" + count);
        }
        return data;

    }
    public JSONObject createJson(String categoryName){
        String userInput = "Valor";
        JSONObject attribute = new JSONObject();
        //Una clase, método o campo declarado como estático puede ser accedido o invocado sin la necesidad de tener que instanciar un objeto de la clase
        // Scanner prompt = new Scanner(System.in);

        // Array List es de tamaño flexible y de distintos datos
        ArrayList<String> inputs = new ArrayList<String>();
        System.out.println("Write the " + categoryName +" you want to add or press enter to finish");
        while (userInput != "") {
            System.out.println("Enter a " + categoryName +" and press Enter");
            userInput = this.prompt.nextLine();  // Read user input
            if (userInput != "") {
                inputs.add(userInput);
                System.out.println("The New " + categoryName +" is: " + userInput);
            }
        }
        Integer count = 1;
        for (String element : inputs) {
            System.out.println("Select a model for " + element);
            System.out.println("Type 1 for creature model");
            System.out.println("Type 2 for element model");
            System.out.println("Type 3 for item model");
            userInput = this.prompt.nextLine();
            // TODO validar que ponga un integer
            Map data = this.addAttributes(count++, Integer.valueOf(userInput));
            org.json.simple.JSONObject jsonObject = new JSONObject(data);
            attribute.put(element, jsonObject);
        }
        System.out.println(attribute);
        return attribute;
    }


}
