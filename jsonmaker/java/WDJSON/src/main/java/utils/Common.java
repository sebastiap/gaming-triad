package utils;

import java.util.ArrayList;
import java.util.Scanner;

public class Common {
    public static ArrayList<String> repeatUntilBlank(){

        Scanner prompt = new Scanner(System.in);
        String userInput = "Valor";
        ArrayList<String> elemList = new ArrayList<String>();
        System.out.println("Write the attributes you want to add or press enter to finish");
        while (userInput != "") {
        System.out.println("Enter the name of an atributte and press enter");
        userInput = prompt.nextLine();
        if (userInput != "") {
            elemList.add(userInput);
        }
    }
        return elemList;
}
}
