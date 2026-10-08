using Common.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Common.Database
{
    public class SQLiteDatabase : IDatabase, IDisposable
    {
        private ApiaryContext context;

        public SQLiteDatabase()
        {
            context = new ApiaryContext();
        }

        public void Dispose()
        {
            context?.Dispose();
        }

        public void Delete(int productID)
        {
            Product? product = context.Products.Where(x => x.ID == productID).FirstOrDefault();

            if (product == null)
                throw new KeyNotFoundException($"Product with ID = {productID} is not found");

            context.Products.Remove(product);
        }

        public IEnumerable<Product> List()
        {
            return context.Products.ToList();
        }

        public void Store(Product product)
        {
            context.Products.Add(product);
            context.SaveChanges();
        }

        public void Update(Product product)
        {
            context.Products.Update(product);
            context.SaveChanges();
        }
    }
}
