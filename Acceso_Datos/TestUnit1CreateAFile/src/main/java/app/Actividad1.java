package app;

import java.io.RandomAccessFile;
import java.util.Scanner;

public class Actividad1 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String nombreArchivo = "src/main/resources/ejemplo2.bin";
        try{
            RandomAccessFile raf = new RandomAccessFile(nombreArchivo, "rw");


            for (int i = 0; i < 10; i++){
                raf.writeInt(i);
            }

            int pos = sc.nextInt();


            int nuevoValor = sc.nextInt();

            raf.seek(pos);

            raf.writeInt(nuevoValor);


            System.out.println(raf.readInt());

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
