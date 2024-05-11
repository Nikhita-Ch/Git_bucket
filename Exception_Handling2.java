public class Exception_Handling2 {
    public static int divide(int dividend, int divisor) throws ArithmeticException {
        if (divisor == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return dividend / divisor;
    }
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException caught: Division by zero");
            e.printStackTrace();
        }

        try{
            String S1= null;
            System.out.println(S1.length());
        }
        catch(NullPointerException f){
            System.out.println("Caught NullPointerException: "+ f.getMessage());
            f.printStackTrace();
        }

        try{
            int[] arr= {9,0,3,45};
            System.out.println(arr[2]);
            System.out.println(arr[10]);
        }
        catch(ArrayIndexOutOfBoundsException g){
            System.out.println("caught ArrayIndexOutOfBoundsException: "+ g.getMessage());
            g.printStackTrace();
        }

        try{
            int age= -11;
            if(age<0){
                throw new IllegalArgumentException("age cannot be negative");
            }
        }
        catch(IllegalArgumentException h){
            System.out.println("found Exception of an illegal arguement" + h.getMessage());
            h.printStackTrace();
        }

        // try{
        //     int a=2; int b=4;
        //     add(a, b);
        // }
        // catch(NoSuchMethodException i){
        //     System.out.println("Method notfound...");
        //     i.printStackTrace();
        // }
    }

    
}