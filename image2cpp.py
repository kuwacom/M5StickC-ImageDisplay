import argparse
from PIL import Image
import numpy as np

def convertImageToCpp(inputFile, outputName, width, height):
    img = Image.open(inputFile)

    img = img.convert('RGB')
    img = img.resize((width, height))  # リサイズ

    imgData = np.array(img)

    # C++の配列形式に変換
    with open(outputName + ".h", "w") as f:
        f.write("#ifndef " + outputName.upper() + "_H\n")
        f.write("#define " + outputName.upper() + "_H\n")
        f.write("extern const uint8_t " + outputName + "[] = {\n")
        
        # 各ピクセルのRGBを1つのバイトとして配列に保存
        flatData = imgData.flatten()
        hexData = []
        for i in range(0, len(flatData), 3):  # RGBの順番で1ピクセル3バイト
            r = flatData[i]
            g = flatData[i + 1]
            b = flatData[i + 2]
            # hexData.append(f"0x{r:02X}, 0x{g:02X}, 0x{b:02X}")
            hexData.append(f"{r},{g},{b}")
        
        f.write(",".join(hexData))
        
        f.write("\n};\n")
        f.write("#endif")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="画像をC++のRGB配列形式に変換")
    parser.add_argument("inputFile", help="入力画像ファイル（PNGやBMPなど）")
    parser.add_argument("outputName", help="出力C++ヘッダーファイル名")
    
    # 表示するときのサイズ
    parser.add_argument("--width", type=int, default=160, help="画像の幅（デフォルト: 160）")
    parser.add_argument("--height", type=int, default=80, help="画像の高さ（デフォルト: 80）")
    
    args = parser.parse_args()
    
    # 画像を指定サイズにリサイズしてC++ヘッダー形式に変換
    convertImageToCpp(args.inputFile, args.outputName, args.width, args.height)
