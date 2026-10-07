using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using System;
using System.Collections.Generic;
using System.Drawing.Imaging;
using System.Drawing;
using System.Text;

namespace Common.Util
{
    public class ImageToBytesConverter : ValueConverter<Image, byte[]>
    {
        public ImageToBytesConverter() : base(
            img => ImageToBytes(img),
            bytes => BytesToImage(bytes))
        { }

        private static byte[] ImageToBytes(Image img)
        {
            using var ms = new MemoryStream();
            img.Save(ms, ImageFormat.Png);
            return ms.ToArray();
        }

        private static Image BytesToImage(byte[] bytes)
        {
            if (bytes == null || bytes.Length == 0)
            {
                return null;
            }

            using var ms = new MemoryStream(bytes);
            return Image.FromStream(ms);
        }
    }
}
