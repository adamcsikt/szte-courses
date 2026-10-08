using Common.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Common.Database
{
    public class InMemoryDatabase : IDatabase
    {
        private int lastID = 0;
        private List<Product> Products { get; set; }

        public InMemoryDatabase()
        {
            Products = new List<Product>();
        }

        public void Delete(int productID)
        {
            var storedProduct = SearchByID(productID);
            Products.Remove(storedProduct);
        }

        public IEnumerable<Product> List()
        {
            return Products;
        }

        public void Store(Product product)
        {
            if (product.ID != 0)
                throw new Exception("Something went wrong: The given product is already in the database");

            product.ID = lastID++;
            Products.Add(product);
        }

        public void Update(Product product)
        {
            var storedProduct = SearchByID(product.ID);

            storedProduct.Name = product.Name;
            storedProduct.Description = product.Description;
            storedProduct.Price = product.Price;
            storedProduct.PackagingDate = product.PackagingDate;
            storedProduct.ExpirationDate = product.ExpirationDate;
            storedProduct.Image = product.Image;
        }

        private Product SearchByID(int productID)
        {
            var storedProduct = Products.Where(x => x.ID == productID).SingleOrDefault();

            if (storedProduct == null)
                throw new KeyNotFoundException($"Product with ID = {productID} is not found");

            return storedProduct;
        }
    }
}
