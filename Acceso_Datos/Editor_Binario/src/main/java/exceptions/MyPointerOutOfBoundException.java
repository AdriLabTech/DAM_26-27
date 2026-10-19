package exceptions;

public class MyPointerOutOfBoundException extends Exception{
    public MyPointerOutOfBoundException(){
        System.out.println("The index of pointer is bigger than the file lenght");
    }
}
