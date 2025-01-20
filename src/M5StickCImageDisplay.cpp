#include "M5StickCImageDisplay.h"

M5StickCImageDisplay::M5StickCImageDisplay(int width, int height)
{
    this->width = width;
    this->height = height;
}

// 画像データをディスプレイに表示
void M5StickCImageDisplay::displayImage(const uint8_t *imageData)
{
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            int index = (y * width + x) * 3;  // 各ピクセルRGBで3バイト分
            uint8_t r = imageData[index];     // 赤
            uint8_t g = imageData[index + 1]; // 緑
            uint8_t b = imageData[index + 2]; // 青

            M5.Lcd.drawPixel(x, y, M5.Lcd.color565(r, g, b)); // ピクセル描画
        }
    }
}
