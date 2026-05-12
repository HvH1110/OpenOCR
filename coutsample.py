def count_samples(file_path):
    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip(): # As long as the line isn't totally blank
                line_count += 1
    print(f"Total image samples in txt file: {line_count}")

count_samples('C:/DAIHOC/OpenOCR/OpenOCR/vintext/text_recognition_data/text_recognition_data/test_data.txt')