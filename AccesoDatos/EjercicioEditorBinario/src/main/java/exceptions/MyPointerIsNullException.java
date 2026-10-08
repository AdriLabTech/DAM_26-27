package exceptions;

public class MyPointerIsNullException extends Exception{
    public MyPointerIsNullException(){
        System.out.println("The index pointer is null and is not possible seek to null position");
    }
}
