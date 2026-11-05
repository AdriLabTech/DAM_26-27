package app;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.RandomAccessFile;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
         String nombreArchivo = "src/main/resources/ejemplo1.txt";

         try{
             RandomAccessFile raf = new RandomAccessFile(nombreArchivo, "rw");
             raf.setLength(8);
             raf.seek(0);
             raf.write("saludo".getBytes(StandardCharsets.UTF_8));

             //raf.seek(4 * (2 - 1));
             raf.seek(6);
             raf.writeByte(117);

             raf.seek(7);
             raf.writeByte(117);

             raf.seek(8);
             raf.writeByte(117);
             //raf.seek(0);



             System.out.println(raf.getFilePointer());

             raf.seek(0);

             System.out.println(raf.readLine());

         }catch (Exception e){
             e.printStackTrace();
         }
    }
}
