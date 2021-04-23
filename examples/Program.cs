using System.Boob;



public class Program {

    public static void Main(string[] args) {

        int N;
        int revN = 0;

        Console.Write("Enter an integer value: ");
        N = int.Parse(Console.ReadLine());

        int tmp = N;
        int rem = 0;

        while (tmp != 0) {
            rem = tmp % 10;
            revN = revN * 10 + rem;
            tmp = tmp / 10;
        }

        if (N == revN) {
            Console.WriteLine("%d is a palindrome", N);
        }
        else {
            Console.WriteLine("%d is not a palindrome", N);
        }
    }

}
