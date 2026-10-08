namespace Administration
{
    partial class ProductAdd
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            name = new TextBox();
            description = new TextBox();
            price = new TextBox();
            packagingDate = new DateTimePicker();
            expirationDate = new DateTimePicker();
            selectImageButton = new Button();
            pictureBox = new PictureBox();
            saveButton = new Button();
            cancelButton = new Button();
            errorProvider = new ErrorProvider(components);
            openFileDialog = new OpenFileDialog();
            deleteButton = new Button();
            ((System.ComponentModel.ISupportInitialize)pictureBox).BeginInit();
            ((System.ComponentModel.ISupportInitialize)errorProvider).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(95, 28);
            label1.Name = "label1";
            label1.Size = new Size(63, 25);
            label1.TabIndex = 0;
            label1.Text = "Name:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(52, 65);
            label2.Name = "label2";
            label2.Size = new Size(106, 25);
            label2.TabIndex = 1;
            label2.Text = "Description:";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(105, 207);
            label3.Name = "label3";
            label3.Size = new Size(53, 25);
            label3.TabIndex = 2;
            label3.Text = "Price:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(20, 246);
            label4.Name = "label4";
            label4.Size = new Size(138, 25);
            label4.TabIndex = 3;
            label4.Text = "Packaging Date:";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(22, 285);
            label5.Name = "label5";
            label5.Size = new Size(136, 25);
            label5.TabIndex = 4;
            label5.Text = "Expiration Date:";
            // 
            // name
            // 
            name.Location = new Point(164, 25);
            name.Name = "name";
            name.Size = new Size(592, 31);
            name.TabIndex = 5;
            // 
            // description
            // 
            description.Location = new Point(164, 59);
            description.Multiline = true;
            description.Name = "description";
            description.Size = new Size(592, 138);
            description.TabIndex = 6;
            // 
            // price
            // 
            price.Location = new Point(164, 201);
            price.Name = "price";
            price.PlaceholderText = "0,00 Ft";
            price.Size = new Size(592, 31);
            price.TabIndex = 7;
            price.TextChanged += ValidatePrice;
            // 
            // packagingDate
            // 
            packagingDate.Location = new Point(164, 241);
            packagingDate.Name = "packagingDate";
            packagingDate.Size = new Size(592, 31);
            packagingDate.TabIndex = 8;
            // 
            // expirationDate
            // 
            expirationDate.Location = new Point(164, 279);
            expirationDate.Name = "expirationDate";
            expirationDate.Size = new Size(592, 31);
            expirationDate.TabIndex = 9;
            // 
            // selectImageButton
            // 
            selectImageButton.Location = new Point(16, 322);
            selectImageButton.Name = "selectImageButton";
            selectImageButton.Size = new Size(142, 34);
            selectImageButton.TabIndex = 10;
            selectImageButton.Text = "Select Image";
            selectImageButton.UseVisualStyleBackColor = true;
            selectImageButton.Click += OpenFile;
            // 
            // pictureBox
            // 
            pictureBox.Location = new Point(164, 322);
            pictureBox.Name = "pictureBox";
            pictureBox.Size = new Size(592, 213);
            pictureBox.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox.TabIndex = 11;
            pictureBox.TabStop = false;
            // 
            // saveButton
            // 
            saveButton.BackColor = Color.FromArgb(128, 255, 128);
            saveButton.Location = new Point(676, 575);
            saveButton.Name = "saveButton";
            saveButton.Size = new Size(112, 34);
            saveButton.TabIndex = 12;
            saveButton.Text = "Save";
            saveButton.UseVisualStyleBackColor = false;
            saveButton.Click += SaveProduct;
            // 
            // cancelButton
            // 
            cancelButton.BackColor = Color.FromArgb(255, 128, 128);
            cancelButton.Location = new Point(560, 575);
            cancelButton.Name = "cancelButton";
            cancelButton.Size = new Size(110, 34);
            cancelButton.TabIndex = 13;
            cancelButton.Text = "Cancel";
            cancelButton.UseVisualStyleBackColor = false;
            // 
            // errorProvider
            // 
            errorProvider.ContainerControl = this;
            // 
            // openFileDialog
            // 
            openFileDialog.FilterIndex = 2;
            openFileDialog.Title = "Select Image";
            // 
            // deleteButton
            // 
            deleteButton.BackColor = Color.Red;
            deleteButton.Location = new Point(442, 575);
            deleteButton.Name = "deleteButton";
            deleteButton.Size = new Size(112, 34);
            deleteButton.TabIndex = 14;
            deleteButton.Text = "Delete";
            deleteButton.UseVisualStyleBackColor = false;
            deleteButton.Visible = false;
            deleteButton.Click += DeleteProduct;
            // 
            // ProductAdd
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 621);
            Controls.Add(deleteButton);
            Controls.Add(cancelButton);
            Controls.Add(saveButton);
            Controls.Add(pictureBox);
            Controls.Add(selectImageButton);
            Controls.Add(expirationDate);
            Controls.Add(packagingDate);
            Controls.Add(price);
            Controls.Add(description);
            Controls.Add(name);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "ProductAdd";
            Text = "Add Product";
            Load += Loaded;
            ((System.ComponentModel.ISupportInitialize)pictureBox).EndInit();
            ((System.ComponentModel.ISupportInitialize)errorProvider).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private TextBox name;
        private TextBox description;
        private TextBox price;
        private DateTimePicker packagingDate;
        private DateTimePicker expirationDate;
        private Button selectImageButton;
        private PictureBox pictureBox;
        private Button saveButton;
        private Button cancelButton;
        private ErrorProvider errorProvider;
        private OpenFileDialog openFileDialog;
        private Button deleteButton;
    }
}