using Common.Database;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Text;
using System.Windows.Forms;
using Common.Models;

namespace Administration
{
    public partial class ProductAdd : Form
    {
        private readonly IDatabase database;
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Product? Product { get; set; } = null;
        public ProductAdd(IDatabase db)
        {
            this.database = db;
            InitializeComponent();

            packagingDate.MaxDate = DateTime.Today;

            expirationDate.MinDate = packagingDate.Value;
            expirationDate.Value = packagingDate.Value.AddDays(90);

            packagingDate.ValueChanged += (sender, e) =>
            {
                expirationDate.MinDate = packagingDate.Value;
            };

            string separator = string.Empty;
            var codecs = ImageCodecInfo.GetImageEncoders();
            foreach (var c in codecs)
            {
                string codecName = c.CodecName[8..].Replace("Codec", "Files").Trim();
                openFileDialog.Filter = String.Format("{0}{1}{2} ({3})|{3}", openFileDialog.Filter, separator, codecName, c.FilenameExtension);
                separator = "|";
            }
        }

        private void ValidatePrice(object sender, EventArgs e)
        {
            if (price.Text.Length > 0 && !float.TryParse(price.Text, out var _))
                errorProvider.SetError(price, $"{price.Text} is not valid numerical value for HUF currency!");
            else
                errorProvider.SetError(price, string.Empty);
        }

        private void SaveProduct(object sender, EventArgs e)
        {
            errorProvider.Clear();

            string productName = name.Text;
            string productDescription = description.Text;
            float productPrice = float.TryParse(price.Text, out var priceValue) ? priceValue : 0;
            DateTime productPackaged = packagingDate.Value;
            DateTime productExpires = expirationDate.Value;
            Image productImage = pictureBox.Image;

            if (productName.Length == 0)
                errorProvider.SetError(name, "Name is required");

            if (productDescription.Length == 0)
                errorProvider.SetError(description, "Description is required");

            if (price.Text.Length == 0)
                errorProvider.SetError(price, "Will this product be free?");
            else if (!float.TryParse(price.Text, out float _productPrice))
                errorProvider.SetError(price, $"{price.Text} is not valid numerical value for HUF currency!");

            Action<Product> action = (Product == null) ? database.Store : database.Update;
            Product ??= new Product(); // compound assignment

            Product.Name = productName;
            Product.Description = productDescription;
            Product.Price = productPrice;
            Product.PackagingDate = productPackaged;
            Product.ExpirationDate = productExpires;
            Product.Image = productImage;

            action(Product);

            DialogResult = DialogResult.OK;
        }

        private void OpenFile(object sender, EventArgs e)
        {
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                pictureBox.Image = Image.FromFile(openFileDialog.FileName);
            }
        }

        private void Loaded(object sender, EventArgs e)
        {
            if (Product != null)
            {
                name.Text = Product.Name;
                description.Text = Product.Description;
                price.Text = Product.Price.ToString();

                packagingDate.Value = Product.PackagingDate;
                expirationDate.Value = Product.ExpirationDate;
                pictureBox.Image = Product.Image;

                deleteButton.Visible = true;
            }
        }

        private void DeleteProduct(object sender, EventArgs e)
        {
            database.Delete(Product.ID);

            DialogResult = DialogResult.OK;
        }
    }
}
