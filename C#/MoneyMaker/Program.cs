using System;

namespace MoneyMaker
{
  class MainClass
  {
    public static void Main(string[] args)
    {
      Console.WriteLine("Welcome to Money Maker!");
      Console.WriteLine("How much money to convert?");
      string moneyString = Console.ReadLine();
      double moneyConvert = Convert.ToDouble(moneyString);
      Console.WriteLine($"To be converted: {moneyConvert}");
      int goldCoin = 10;
      int silverCoin = 5;
      double goldCoins = Math.Floor(moneyConvert / goldCoin);
      double remainderGoldCoin = Math.Floor(moneyConvert % goldCoin);
      double silverCoins = Math.Floor(remainderGoldCoin /  silverCoin);
      double bronzeCoins = Math.Floor(remainderGoldCoin % silverCoin);

      Console.WriteLine($"Gold Coins = {goldCoins} \n Silver Coins = {silverCoins} \n Bronze Coins = {bronzeCoins}");
      
    }
  }
}
