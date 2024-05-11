public class Threads2 extends Thread{
    public void run(){
        for (int i=10; i>=1; i--){
            System.out.println("h" +i);
            try{
                Thread.sleep(500);
            }catch(Exception e){};
        }
    }
}
