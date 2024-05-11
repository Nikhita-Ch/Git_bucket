public class Threads1 implements Runnable{
    public void run(){
        for(int i=1; i<=10; i++){
            System.out.println(i);
            try{
                Thread.sleep(1000);
            }
            catch(Exception e){}
        }
    }

    public static void main(String[] args) {
        Threads1 t= new Threads1(); 
        Thread thr= new Thread(t);
        Threads2 t2= new Threads2();
        thr.start();
        t2.start();
    }
}
