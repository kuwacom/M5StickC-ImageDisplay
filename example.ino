#include <M5StickC.h>
#include "src/M5StickCImageDisplay.h"

#include "winXP.h" // 生成したヘッダーファイルをインクルード

const int width = 160; // 画像の幅（M5StickCのディスプレイサイズに合わせて調整）
const int height = 80; // 画像の高さ（M5StickCのディスプレイサイズに合わせて調整）

M5StickCImageDisplay imageDisplay(width, height);

void setup()
{
    M5.begin();
    M5.Lcd.setRotation(1);

    imageDisplay.displayImage(winXP); // 画像を表示
}

void loop()
{
}
