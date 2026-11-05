package ejercicios;

import java.io.IOException;
import java.io.RandomAccessFile;


public class Ejercicio1 {
    static String fileName = "src/main/resources/exercise2.bin";
    // Modify a binary file that contain a list of integer numbers
    public static void main(String[] args){

        try{
            addNumberIntoFile(10);
            addNumberIntoFile(20);
            addNumberIntoFile(30);
            addNumberIntoFile(40);
            addNumberIntoFile(50);
            addNumberIntoFile(60);
            addNumberIntoFile(65);
            addNumberIntoFile(80);

        }catch (Exception e){
            e.printStackTrace();
        }
    }

    private static void addNumberIntoFile(int number, Long idxPointer){
        try (RandomAccessFile raf = new RandomAccessFile(fileName, "rw")){
            if (idxPointer != null){
                raf.seek(4 * (idxPointer - 1));
            }else{
                raf.seek(raf.length());
            }

            raf.writeInt(number);
        }catch (IOException io){
            io.printStackTrace();
        }
    }

    private static void addNumberIntoFile(int number){
        addNumberIntoFile(number, null);
    }

    private static void showNumbersFile(){

    }


}
