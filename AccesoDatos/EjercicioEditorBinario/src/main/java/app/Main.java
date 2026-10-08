package app;

import exceptions.MyFileNotFoundException;
import exceptions.MyPointerIsNullException;
import exceptions.MyPointerOutOfBoundException;
import utils.Utils;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Main {
    private static String filePath = "src/main/resources/exerciseBinary.bin";
    private static final File file = new File(filePath);

    public static void main (String[] args){
        try {
            initializeFile();
            showContentFile();
            modifyNumber(Utils.askUserForNumber("Set the new number that you want introduce into the file: "),
                    Utils.askUserForPointerPosition("Set the pointer position: "));
            showContentFile();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void showContentFile() throws MyFileNotFoundException {
        try (RandomAccessFile raf = new RandomAccessFile(filePath,"r")){
            System.out.println("File: " + file.getName() + " (" + file.getPath() + ")");

            for(int i = 0; i < raf.length() / 4; i ++) {
                raf.seek(4 * i);
                System.out.println("Position: " + (i + 1) + "| Content: " + raf.readInt());
            }
        } catch (IOException e){
            throw new MyFileNotFoundException();
        }
    }

    private static void initializeFile(){
        try(RandomAccessFile raf = new RandomAccessFile(filePath, "rw")){
            if (raf.length() > 0){
                return;
            }

            addNumberIntoFile(10);
            addNumberIntoFile(20);
            addNumberIntoFile(30);
            addNumberIntoFile(40);
            addNumberIntoFile(50);
            addNumberIntoFile(60);
            addNumberIntoFile(70);
            addNumberIntoFile(80);
            addNumberIntoFile(90);
            addNumberIntoFile(95);

        }catch (Exception e){
            e.printStackTrace();
        }
    }

    private static void modifyNumber(int newNumber, Long idxPointer){
        try(RandomAccessFile raf = new RandomAccessFile(filePath, "rw")){

            if (idxPointer == null){
                throw new MyPointerIsNullException();
            }
            else if (raf.length() < 4 * (idxPointer - 1 )){
                throw new MyPointerOutOfBoundException();
            }

            else{
                addNumberIntoFile(newNumber, idxPointer);
            }

        }catch (IOException e){
            e.printStackTrace();
        } catch (MyPointerOutOfBoundException | MyPointerIsNullException e) {
            throw new RuntimeException(e);
        }
    }

    private static void addNumberIntoFile(int number, Long idxPointer){
        try(RandomAccessFile raf = new RandomAccessFile(filePath, "rw")){

            if (idxPointer != null && idxPointer > 0){
                raf.seek(4 * (idxPointer - 1));
            }else{
                raf.seek(raf.length());
            }

            raf.writeInt(number);

        }catch (IOException e){
            e.printStackTrace();
        }
    }

    private static void addNumberIntoFile(int number){
        addNumberIntoFile(number, null);
    }
}
