namespace filtrowanie_obrazu
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void OpenFileBtn_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Image Files (*.BMP; *.JPG; *.JPEG; *.GIF; *.PNG)| *.BMP; *.JPG; *.JPEG; *.GIF; *.PNG";
            openFileDialog.InitialDirectory = @"C:\";

            DialogResult result = openFileDialog.ShowDialog();

            if (result == DialogResult.OK)
            {
                string fileName = openFileDialog.FileName;
                Image image = Image.FromFile(fileName);
                pictureBox1.Image = image;
            }
        }

        private void SharpeningBtn_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
            {
                MessageBox.Show("Brak za³adowanego obrazu");
                return;
            }

            Bitmap bitmap = new Bitmap(pictureBox1.Image);

            for (int x = 1; x < bitmap.Width - 1; x++)
            {
                for (int y = 1; y < bitmap.Height - 1; y++)
                {
                    Color pixelColor = bitmap.GetPixel(x, y);
                    int red = pixelColor.R * 5 - bitmap.GetPixel(x - 1, y).R - bitmap.GetPixel(x + 1, y).R - bitmap.GetPixel(x, y - 1).R - bitmap.GetPixel(x, y + 1).R;
                    int green = pixelColor.G * 5 - bitmap.GetPixel(x - 1, y).G - bitmap.GetPixel(x + 1, y).G - bitmap.GetPixel(x, y - 1).G - bitmap.GetPixel(x, y + 1).G;
                    int blue = pixelColor.B * 5 - bitmap.GetPixel(x - 1, y).B - bitmap.GetPixel(x + 1, y).B - bitmap.GetPixel(x, y - 1).B - bitmap.GetPixel(x, y + 1).B;
                    red = Math.Max(0, Math.Min(255, red));
                    green = Math.Max(0, Math.Min(255, green));
                    blue = Math.Max(0, Math.Min(255, blue));
                    Color newColor = Color.FromArgb(red, green, blue);

                    bitmap.SetPixel(x, y, newColor);
                }
            }
            pictureBox1.Image = bitmap;
        }

        private void GrayscaleBtn_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
            {
                MessageBox.Show("Brak za³adowanego obrazu");
                return;
            }

            Bitmap bitmap = new Bitmap(pictureBox1.Image);

            for (int x = 0; x < bitmap.Width; x++)
            {
                for (int y = 0; y < bitmap.Height; y++)
                {
                    Color pixelColor = bitmap.GetPixel(x, y);
                    int grayValue = (int)((pixelColor.R * 0.3) + (pixelColor.G * 0.59) + (pixelColor.B * 0.11));
                    Color newColor = Color.FromArgb(grayValue, grayValue, grayValue);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            pictureBox1.Image = bitmap;
        }

        private void SaveImageBtn_Click(object sender, EventArgs e)
        {
            Bitmap bitmap = new Bitmap(pictureBox1.Image);

            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "JPEG Image|*.jpg|Bitmap Image|*.bmp|PNG Image|*.png";
            saveFileDialog.Title = "Save an Image File";
            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                bitmap.Save(saveFileDialog.FileName);
            }
        }
    }
 }
