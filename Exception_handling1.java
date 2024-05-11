/**
 * Exception_handling1
 */
public class Exception_handling1 {

    public static void main(String[] args) {
        try{
        System.out.println(1/2);
        System.out.println(1/0);
        }catch(NullPointerException | ArithmeticException e){
            System.out.println(e.getMessage());
        }
    }
}