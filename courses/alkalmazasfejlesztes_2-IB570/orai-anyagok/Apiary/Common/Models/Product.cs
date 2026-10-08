using System;
using System.Collections.Generic;
using System.Text;

namespace Common.Models
{
    public class Product
    {
        public int ID { get; set; }
        public string? Name { get; set; }
        public string? Description { get; set; }
        public float Price { get; set; }
        public System.Drawing.Image? Image { get; set; }
        public DateTime PackagingDate { get; set; }
        public DateTime ExpirationDate { get; set; }
    }
}
