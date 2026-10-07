using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace Administration
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.SetHighDpiMode(HighDpiMode.SystemAware);

            var host = Host.CreateDefaultBuilder()
                .ConfigureServices((context, services) =>
                {
                    services.AddSingleton<Common.Database.IDatabase, Common.Database.SQLiteDatabase>();
                    services.AddTransient<Form1>();
                    services.AddTransient<ProductAdd>();
                }).Build();

            using var serviceScope = host.Services.CreateScope();
            var startForm = serviceScope.ServiceProvider.GetRequiredService<Form1>();

            Application.Run(startForm);
        }
    }
}