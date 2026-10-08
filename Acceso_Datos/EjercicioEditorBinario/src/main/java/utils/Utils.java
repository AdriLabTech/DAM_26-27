package utils;

import exceptions.MyPointerIsNullException;

import java.util.Scanner;

public class Utils {
    private static Scanner s = new Scanner(System.in);
    public static int askUserForNumber(String msg){
        System.out.println(msg);
        return s.nextInt();
    }

    public static Long askUserForPointerPosition(String msg) throws MyPointerIsNullException {
        System.out.println(msg);
        try {
            return s.nextLong();
        } catch (Exception e) {
            MyPointerIsNullException ex = new MyPointerIsNullException();
            return 0L;
        }
    }
}
