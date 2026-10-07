using Common.Models;
using Common.Util;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Text;
using Common.Util;

namespace Common.Database
{
    public class ApiaryContext : DbContext
    {
        public DbSet<Product> Products { get; set; }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            //okt.inf.szte.hu-s javaslat
            //optionsBuilder.UseSqlite("Data Source=absolute/path/to/the/apiary.sqlite");

            // ha jól működik a lenti, akkor a következő sorokat lehet használni a helyi AppData mappában történő tároláshoz
            string localAppData =
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);

            string databaseDirectory =
                Path.Combine(localAppData, "Apiary", "db");

            Directory.CreateDirectory(databaseDirectory);

            string databasePath =
                Path.Combine(databaseDirectory, "apiary.sqlite");

            optionsBuilder.UseSqlite($"Data Source={databasePath}");
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Product>()
                .Property(p => p.Image)
                .HasConversion<ImageToBytesConverter>();
        }
    }
}
