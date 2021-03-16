using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;

namespace micro_cms_v2
{
    class Program
    {
        static void Main(string[] args)
        {
            var webDriver = LaunchBrowser();
            try
            {
                // This is where we can start interacting with the browser
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

            var driver = new ChromeDriver(options);
            return driver;
        }
    }
}
