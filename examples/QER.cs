using System;



namespace CS_tmp {

    class QER {

        public static void Main() {

            double A, B, C, D, r1, r2, real, imag;

            Console.WriteLine("Enter coefs A, B, and C: ");
            A = double.Parse(Console.ReadLine());
            B = double.Parse(Console.ReadLine());
            C = double.Parse(Console.ReadLine());

            D = B * B - 4 * A * C;

            if (D > 0) {
                r1 = (-B + Math.Sqrt(D)) / (2 * A);
                r2 = (-B - Math.Sqrt(D)) / (2 * A);
                Console.WriteLine("root1 = %f, root2 = %f", r1, r2);
            }
            else if (D == 0) {
                r1 = -B / (2 * A);
                Console.WriteLine("root1 = root2 = %f", r1);
            }
            else {
                real = -B / (2 * A);
                imag = Math.Sqrt(-D) / (2 * A);
                Console.WriteLine("root1 = %f + %fi, root2 = %f - %fi", real, imag, real, imag);
            }
        }

    }

}
