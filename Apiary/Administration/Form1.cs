using Common.Database;
using Common.Models;
using Microsoft.Extensions.DependencyInjection;

namespace Administration
{
    public partial class Form1 : Form
    {
        private readonly IServiceProvider serviceProvider;
        public Form1(IServiceProvider _serviceProvider)
        {
            serviceProvider = _serviceProvider;
            InitializeComponent();
        }

        private void AddProduct(object sender, EventArgs e)
        {
            using var window = serviceProvider.GetRequiredService<ProductAdd>();
            window.ShowDialog();

            if (window.DialogResult == DialogResult.OK)
                UpdateGridView();
        }

        private void ListProducts(object sender, EventArgs e)
        {
            title.Visible = true;
            title.Text = "Products";

            UpdateGridView();
        }

        private void UpdateGridView()
        {
            var database = serviceProvider.GetRequiredService<IDatabase>();

            dataGridView.DataSource = null;
            dataGridView.DataSource = database.List();

            dataGridView.Columns["ID"].Visible = false;
            dataGridView.Columns["Image"].Visible = false;
        }

        private void EditProduct(object sender, DataGridViewCellMouseEventArgs e)
        {
            if (dataGridView.CurrentRow?.DataBoundItem is not Product product)
                return;

            using var window = serviceProvider.GetRequiredService<ProductAdd>();
            window.Product = product;
            window.ShowDialog();

            if (window.DialogResult == DialogResult.OK)
                UpdateGridView();
        }
    }
}
