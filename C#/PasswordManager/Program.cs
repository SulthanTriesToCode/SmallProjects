using System;

namespace PasswordChecker
{
  class Program
  {
    public static void Main(string[] args)
    {
        // Print 'Enter Password:'
        Console.WriteLine("Enter Password:");
        // Declare string 'password' and set it to the user input
        string password = Console.ReadLine();
        // Declare integer as minLength
        int minLength = 8;
        // Declare string = uppercase
        string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        // Declare string = lowercase
        string lowercase = "abcdefghijklmnopqrstuvwxyz";
        // Declare string = digits
        string digits = "1234567890";
        // Declare string = specialChars
        string specialChars = "!@#$%^&*()_+";
        // Declare integer = score
        int score = 0;

        // if password is greater than minLength add 1 to score
        if (password.Length >= minLength)
        {
            score++;
        }

        // if password contains uppercase add 1 to score
        if (Tools.Contains(password, uppercase))
        {
            score++;
        }

        // if password contains lowercase add 1 to score
        if (Tools.Contains(password, lowercase))
        {
            score++;
        }

        // if password contains digits add 1 to score
        if (Tools.Contains(password, digits))
        {
            score++;
        }

        // if password contains specialChars add 1 to score
        if (Tools.Contains(password, specialChars))
        {
            score++;
        }

        // if score is bigger than 4, print 'Extremely Strong'
        if (score > 4)
        {
            Console.WriteLine("Extremely Strong");
        }
        // if else score is bigger than 3, print 'Strong'
        else if (score > 3)
        {
            Console.WriteLine("Strong");
        }
        // if else score is bigger than 2, print 'Medium'
        else if (score > 2)
        {
            Console.WriteLine("Medium");
        }
        // if else score is bigger than 1, print 'Weak'
        else if (score > 1)
        {
            Console.WriteLine("Weak");
        }
    }
  }
}
