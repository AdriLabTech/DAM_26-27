package exceptions;

import java.io.IOException;

public class MyFileNotFoundException extends IOException {
    public MyFileNotFoundException(){
        super("File Not Found");
    }

    public MyFileNotFoundException(String msg){
        super(msg);
    }
}
