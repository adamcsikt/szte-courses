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
            // Set the database path relative to the application's execution directory
            string databaseDirectory = Path.Combine(AppContext.BaseDirectory, "db");

            Directory.CreateDirectory(databaseDirectory);

            string databasePath = Path.Combine(databaseDirectory, "apiary.sqlite");

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
