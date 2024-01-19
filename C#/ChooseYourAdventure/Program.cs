using System;

namespace ChooseYourOwnAdventure
{
  class Program
  {
      static void Main(string[] args)
    {
      Console.Write("What is your name?: ");
      string name = Console.ReadLine();
      Console.WriteLine($"Hello, {name}! Welcome to our story.");
      Console.Write("It begins on a cold rainy night. You're sitting in your room and hear a noise coming from down the hall. Do you go investigate?");
      Console.Write("\n");
      Console.Write("Type YES or NO: ");
      string noiseChoice = Console.ReadLine();
      noiseChoice = noiseChoice.ToUpper();
      if (noiseChoice == "NO")
      {
        Console.WriteLine("Not much of an adventure if we don't leave our room! THE END.");
        return;
      }
      else if (noiseChoice == "YES")
      {
        Console.Write("You walk into the hallway and see a light coming from under a door down the hall. You walk towards it. Do you open it or knock?");
        Console.Write("\n");
      }
      Console.Write("Type OPEN or KNOCK: ");
      string doorChoice = Console.ReadLine();
      doorChoice = doorChoice.ToUpper();
      if (doorChoice == "KNOCK")
      {
        Console.Write("A voice behind the door speaks. It says, Answer this riddle:");
        Console.Write("\n");
        Console.Write("Poor people have it. Rich people need it. If you eat it you die. What is it?");
        Console.Write("\n");
        Console.Write("Type your answer: ");
        string riddleAnswer = Console.ReadLine();
        riddleAnswer = riddleAnswer.ToUpper();
        if (riddleAnswer == "NOTHING")
        {
          Console.Write("The door opens and NOTHING is there. You turn off the light and run back to your room and lock the door. THE END.");
          return;
        }
        else
        {
          Console.Write("You answered incorrectly. The door doesn't open. THE END.");
          return;
        }
      } else if (doorChoice == "OPEN")
      {
        Console.Write("The door is locked! See if one of your three keys will open it.");
        Console.Write("\n");
        Console.Write("Enter a number (1-3): ");
        string keyChoice = Console.ReadLine();
        keyChoice = keyChoice.ToUpper();
        switch (keyChoice)
        {
          case "1":
            Console.Write("You choose the first key. Lucky choice! The door opens and NOTHING is there. Strange... THE END.");
            return;
          case "2":
            Console.Write("You choose the second key. The door doesn't open. THE END.");
            return;
          case "3":
            Console.Write("You choose the third key. The door doesn't open. THE END.");
            return;
          default:
            Console.Write("You did not choose a valid key. THE END.");
            return;
        }
      }
    }
  }
}




