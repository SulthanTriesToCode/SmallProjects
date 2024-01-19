using System;

namespace ChooseYourOwnAdventure
{
  class Program
  {
      static void Main(string[] args)
    {
      /* THE MYSTERIOUS NOISE */

      // Start by asking for the user's name:
      Console.Write("What is your name?: ");
      string name = Console.ReadLine();
      Console.WriteLine($"Hello, {name}! Welcome to our story.");
      Console.Write("It begins on a cold rainy night. You're sitting in your room and hear a noise coming from down the hall. Do you go investigate?");
      Console.Write("\n");
      Console.Write("Type YES or NO: ");
      string noiseChoice = Console.ReadLine();
      // turn noisechoice string into uppercase
      noiseChoice = noiseChoice.ToUpper();
      // if noiseChoice is "NO" print, "Not much of an adventure if we don't leave our room! THE END.", then break the program. else if, noiseChoice is "YES" print, "You walk into the hallway and see a light coming from under a door down the hall. You walk towards it. Do you open it or knock?"
      if (noiseChoice == "NO")
      {
        Console.WriteLine("Not much of an adventure if we don't leave our room! THE END.");
      }
      else if (noiseChoice == "YES")
      {
        Console.Write("You walk into the hallway and see a light coming from under a door down the hall. You walk towards it. Do you open it or knock?");
        Console.Write("\n");
      }
    }
  }
}




