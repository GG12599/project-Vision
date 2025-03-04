from paddleocr import PaddleOCR
import pandas as pd

def main():
    # 初始化PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    
    # 读取图片并进行OCR识别
    img_path = '1.webp'
    result = ocr.ocr(img_path, cls=True)
    
    # 提取文字内容
    texts = []
    for line in result:
        for word_info in line:
            text = word_info[1][0]  # 获取识别的文字
            confidence = word_info[1][1]  # 获取置信度
            texts.append({'text': text, 'confidence': confidence})
    
    # 将结果保存到Excel
    df = pd.DataFrame(texts)
    df.to_excel('ocr_result.xlsx', index=False)
    print('OCR识别完成，结果已保存到ocr_result.xlsx')

if __name__ == '__main__':
    main()