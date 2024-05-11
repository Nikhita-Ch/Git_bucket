public class Threads3 {
    public static void main(String[] args) {
        Thread t= Thread.currentThread();
        String name= t.getName();
        System.out.println("thread name is:" +name);
    }
}
