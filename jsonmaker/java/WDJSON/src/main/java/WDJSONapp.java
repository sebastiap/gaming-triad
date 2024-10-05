import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

import clases.Category;
import org.json.simple.JSONObject;
import utils.Common;
import utils.Log;

public class WDJSONapp {

    public static void createFile(String filename,JSONObject content){
        try {
            String filePath = new File("").getAbsolutePath();
            filePath = filePath.concat("/java/WDJSON/public/");
            FileWriter file = new FileWriter(filePath + filename);
            file.write(content.toJSONString());
            file.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println("JSON file created: " + content);
    }

    public static void main(String[] args) {
        String mode;
        Log.main();

        // Inicializo todas las variables necesarias
        Category category = new Category();
        JSONObject atributoJson = new JSONObject();
        String categoryName,filename = "";
        ArrayList<String> listado = new ArrayList<String>();
        Scanner prompt = new Scanner(System.in);
        System.out.println("Select the mode of operation...");
        System.out.println("Type 1 to read attributes.txt file");
        System.out.println("Type 2 to type attributes one by one");

        mode = prompt.nextLine();

        switch (mode) {
            case "1": // Opcion Archivo
                listado = category.readAttributteFile();
                break;
            case "2": // Opcion listado
                listado = Common.repeatUntilBlank();
                break;
            default:
                listado = category.readAttributteFile();
                break;
        }


        for(String l: listado) {
            //categoryName = category.nameCategory();
            categoryName = l;

            // Ver rellenar input para que no siga de largo
            filename = categoryName + ".json";

            atributoJson = category.createJson(categoryName);
            createFile(filename, atributoJson);
        }





    }
}