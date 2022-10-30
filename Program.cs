using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpCrissCross
{
    class Program
    {
        static void Main(string[] args)
        {
            string inputPlayer, inputCPU;
            int randomInt;
            bool playAgain = true;
            //string loop;

            while(playAgain)
            {
                int scorePlayer = 0;
                int scoreCPU = 0;

                while (scorePlayer < 3 && scoreCPU < 3)
                {
                    Console.Write("Choose between ROCK,PAPER and SCISSOR:   ");
                    inputPlayer = Console.ReadLine();
                    inputPlayer = inputPlayer.ToUpper();
                    Random rand = new Random();
                    randomInt = rand.Next(1, 4);
                    switch (randomInt)
                    {
                        case 1:
                            inputCPU = "ROCK";
                            Console.WriteLine("Computer choose ROCK");
                            if (inputPlayer == "ROCK")
                            {
                                Console.WriteLine("DRAW :| \n\n");

                            }
                            else if (inputPlayer == "PAPER")
                            {
                                Console.WriteLine("Player won :) \n\n");
                                scorePlayer++;
                            }
                            else if (inputPlayer == "SCISSOR")
                            {
                                Console.WriteLine("Player Lost :( \n\n");
                                scoreCPU++;
                            }
                            break;
                        case 2:
                            inputCPU = "PAPER";
                            Console.WriteLine("Computer choose PAPER");
                            if (inputPlayer == "PAPER")
                            {
                                Console.WriteLine("DRAW :| \n\n");
                            }
                            else if (inputPlayer == "SCISSOR")
                            {
                                Console.WriteLine("Player won :) \n\n");
                                scorePlayer++;
                            }
                            else if (inputPlayer == "ROCK")
                            {
                                Console.WriteLine("Player Lost :( \n\n");
                                scoreCPU++;
                            }
                            break;
                        case 3:
                            inputCPU = "SCISSOR";
                            Console.WriteLine("Computer choose SCISSOR");
                            if (inputPlayer == "SCISSOR")
                            {
                                Console.WriteLine("DRAW :| \n\n");
                            }
                            else if (inputPlayer == "ROCK")
                            {
                                Console.WriteLine("Player won :) \n\n");
                                scorePlayer++;
                            }
                            else if (inputPlayer == "PAPER")
                            {
                                Console.WriteLine("Player Lost :( \n\n");
                                scoreCPU++;
                            }
                            break;
                        default:
                            Console.WriteLine(" Invalid Entry");
                            break;
                    }
                     Console.WriteLine("\n\nSCORES: \tPLAYER: \t{0} \tCPU: \t{1}",scorePlayer,scoreCPU);
                }
                if (scorePlayer == 3)
                {
                    Console.WriteLine("player won");
                }
                else if (scoreCPU == 3)
                {
                    Console.WriteLine("CPU won");
                }
                else
                {

                }
                Console.WriteLine("Do you want to play again? yes or no");
                string loop = Console.ReadLine();
                if (loop == "yes")
                {
                    playAgain = true;
                }
                else if (loop == "no")
                {
                    playAgain = false;
                }
                else
                {
                    
                }

            }

           
           
        }
    }
}
