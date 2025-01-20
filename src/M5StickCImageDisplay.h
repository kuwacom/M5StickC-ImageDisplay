#ifndef M5STICKC_IMAGEDISPLAY_H
#define M5STICKC_IMAGEDISPLAY_H

#include <M5StickC.h>

class M5StickCImageDisplay
{
public:
    M5StickCImageDisplay(int width, int height);

    void displayImage(const uint8_t *imageData);

private:
    int width;
    int height;
};

#endif // M5StickC_IMAGEDISPLAY_H
