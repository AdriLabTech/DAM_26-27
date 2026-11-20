import java.util.concurrent.CountDownLatch;
public class Carrera2 {
    static int c; static synchronized void incS(){c++;}
    static int prueba(boolean sync) throws Exception {
        c=0; CountDownLatch go=new CountDownLatch(1);
        Runnable r=()->{try{go.await();}catch(Exception e){} for(int i=0;i<1_000_000;i++){ if(sync)incS(); else c++; }};
        Thread a=new Thread(r), b=new Thread(r); a.start(); b.start(); go.countDown(); a.join(); b.join(); return c;
    }
    public static void main(String[] x) throws Exception {
        int mal=0, malS=0; int min=Integer.MAX_VALUE; 
        for(int i=0;i<20;i++){ int v=prueba(false); if(v!=2_000_000)mal++; min=Math.min(min,v); if(prueba(true)!=2_000_000)malS++; if(i<4)System.out.println("sin sync: "+v);}
        System.out.println("20 pruebas -> sin sync erróneas: "+mal+", mínimo "+min+"; con synchronized erróneas: "+malS);
    }
}
