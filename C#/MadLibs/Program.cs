using System;

namespace MadLibs
{
  class Program
  {
    static void Main(string[] args)
    {


      // Let the user know that the program is starting:
      Console.Write("This program is starting.");

      // Give the Mad Lib a title:
      string title = "A Normal Story";
      Console.Write("\n");
      Console.WriteLine(title);
      // Define user input and variables:
      Console.Write("\n");
      Console.Write("Enter name:");
      Console.Write("\n");
      string name = Console.ReadLine();
      Console.Write("\n");
      Console.Write("How are you feeling?");
      Console.Write("\n");
      string feeling = Console.ReadLine();
      Console.Write("\n");
      Console.Write("How is the day going?");
      Console.Write("\n");
      string daystatus = Console.ReadLine();
      Console.Write("\n");
      Console.Write("What kind of people did you see outside?");
      Console.Write("\n");
      string people = Console.ReadLine();
      Console.Write("\n");
      Console.Write("What item did you see in the store?");
      Console.Write("\n");
      string item = Console.ReadLine();
      Console.Write("\n");

      // The template for the story:

      string story = $"This morning {name} woke up feeling {feeling}. 'It is going to be a {daystatus} day!' Outside, a bunch of {people}s were protesting to keep {item} in stores.";


      // Print the story:
      Console.WriteLine(story);

    }
  }
}
