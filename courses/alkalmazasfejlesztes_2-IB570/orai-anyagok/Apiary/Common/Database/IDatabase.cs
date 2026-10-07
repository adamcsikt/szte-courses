using Common.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Common.Database
{
    public interface IDatabase
    {
        public void Store(Product product);
        public void Delete(int productID);
        public void Update(Product product);
        public IEnumerable<Product> List();
    }
}
