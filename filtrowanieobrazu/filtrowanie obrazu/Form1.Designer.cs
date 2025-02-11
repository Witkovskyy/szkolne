namespace filtrowanie_obrazu
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.OpenFileBtn = new System.Windows.Forms.Button();
            this.GrayscaleBtn = new System.Windows.Forms.Button();
            this.SharpeningBtn = new System.Windows.Forms.Button();
            this.SaveImageBtn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.BackColor = System.Drawing.SystemColors.WindowFrame;
            this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 75);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(776, 363);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // OpenFileBtn
            // 
            this.OpenFileBtn.Location = new System.Drawing.Point(12, 19);
            this.OpenFileBtn.Name = "OpenFileBtn";
            this.OpenFileBtn.Size = new System.Drawing.Size(99, 23);
            this.OpenFileBtn.TabIndex = 1;
            this.OpenFileBtn.Text = "Open File";
            this.OpenFileBtn.UseVisualStyleBackColor = true;
            this.OpenFileBtn.Click += new System.EventHandler(this.OpenFileBtn_Click);
            // 
            // GrayscaleBtn
            // 
            this.GrayscaleBtn.Location = new System.Drawing.Point(117, 19);
            this.GrayscaleBtn.Name = "GrayscaleBtn";
            this.GrayscaleBtn.Size = new System.Drawing.Size(75, 23);
            this.GrayscaleBtn.TabIndex = 2;
            this.GrayscaleBtn.Text = "Grayscale";
            this.GrayscaleBtn.UseVisualStyleBackColor = true;
            this.GrayscaleBtn.Click += new System.EventHandler(this.GrayscaleBtn_Click);
            // 
            // SharpeningBtn
            // 
            this.SharpeningBtn.Location = new System.Drawing.Point(198, 19);
            this.SharpeningBtn.Name = "SharpeningBtn";
            this.SharpeningBtn.Size = new System.Drawing.Size(75, 23);
            this.SharpeningBtn.TabIndex = 3;
            this.SharpeningBtn.Text = "Sharpening";
            this.SharpeningBtn.UseVisualStyleBackColor = true;
            this.SharpeningBtn.Click += new System.EventHandler(this.SharpeningBtn_Click);
            // 
            // SaveImageBtn
            // 
            this.SaveImageBtn.Location = new System.Drawing.Point(279, 19);
            this.SaveImageBtn.Name = "SaveImageBtn";
            this.SaveImageBtn.Size = new System.Drawing.Size(75, 23);
            this.SaveImageBtn.TabIndex = 4;
            this.SaveImageBtn.Text = "Save Image";
            this.SaveImageBtn.UseVisualStyleBackColor = true;
            this.SaveImageBtn.Click += new System.EventHandler(this.SaveImageBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.SaveImageBtn);
            this.Controls.Add(this.SharpeningBtn);
            this.Controls.Add(this.GrayscaleBtn);
            this.Controls.Add(this.OpenFileBtn);
            this.Controls.Add(this.pictureBox1);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "Form1";
            this.Text = "Image Filters";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private PictureBox pictureBox1;
        private OpenFileDialog openFileDialog1;
        private Button OpenFileBtn;
        private Button GrayscaleBtn;
        private Button SharpeningBtn;
        private Button SaveImageBtn;
    }
}