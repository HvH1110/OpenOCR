import re

def is_english_and_numbers_only(word):
    """
    Checks if a word contains ONLY standard English letters (A-Z, a-z) and/or numbers (0-9).
    Returns False if it contains Vietnamese characters or special symbols.
    """
    return bool(re.match(r'^[a-zA-Z0-9]+$', word))

def analyze_labels_only(file_path):
    total_words = 0
    valid_words = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                # split(maxsplit=1) finds the first gap (tab or space) and splits the line into exactly 2 parts:
                # parts[0] = "test_images/im1947_1.jpg" (IGNORED)
                # parts[1] = "POMIYA" (ANALYZED)
                parts = line.split(maxsplit=1)
                
                # If there's a file path but no label, skip it
                if len(parts) < 2:
                    continue
                    
                # Extract JUST the label text
                label_text = parts[1]
                
                # Split the label into individual words (if the label has multiple words)
                words = label_text.split()
                
                for word in words:
                    # Clean up standard punctuation attached to the edges of words
                    clean_word = word.strip('.,!?()[]{}"\':;-')
                    
                    if not clean_word:
                        continue
                        
                    total_words += 1
                    
                    if is_english_and_numbers_only(clean_word):
                        valid_words += 1
                        
        if total_words == 0:
            print("No words found in the labels.")
            return

        percentage = (valid_words / total_words) * 100
        
        print(f"--- Results for {file_path} ---")
        print(f"Total words analyzed (ignoring file paths): {total_words}")
        print(f"Words with ONLY English letters & numbers: {valid_words}")
        print(f"Percentage: {percentage:.2f}%")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_path}'. Please check the path.")

# --- Execution ---
analyze_labels_only('C:/DAIHOC/OpenOCR/OpenOCR/vintext/text_recognition_data/text_recognition_data/test_data.txt')