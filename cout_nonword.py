def find_invalid_labels(file_path):
    empty_labels = []
    punctuation_only_labels = []
    total_samples = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                # Keep the exact original line for displaying later, but remove the invisible newline character
                original_line = line.replace('\n', '')
                
                # Strip leading/trailing whitespaces to check if the line is totally blank
                clean_line = line.strip()
                if not clean_line:
                    continue
                    
                total_samples += 1
                
                # Split the line into exactly two parts: [Image Path, Label]
                parts = clean_line.split(maxsplit=1)
                
                # --- CASE 1: Empty Label ---
                # If there is an image path but NO text after it
                if len(parts) < 2:
                    empty_labels.append((line_number, original_line))
                    continue
                
                # --- CASE 2: Non-Word Label (Punctuation Only) ---
                label_text = parts[1]
                
                # Remove all standard punctuation from the label
                stripped_label = label_text.strip('.,!?()[]{}"\':;- ')
                
                # If stripping the punctuation leaves us with absolutely nothing, it's a non-word label
                if not stripped_label:
                    punctuation_only_labels.append((line_number, original_line))

        # --- Print Results ---
        print(f"--- Scan Results for {file_path} ---")
        print(f"Total lines checked: {total_samples}")
        print("-" * 40)
        
        print(f"🛑 EMPTY LABELS FOUND: {len(empty_labels)}")
        for line_num, content in empty_labels:
            print(f"  Line {line_num}: '{content}'")
            
        print(f"\n🛑 PUNCTUATION-ONLY LABELS FOUND: {len(punctuation_only_labels)}")
        for line_num, content in punctuation_only_labels:
            print(f"  Line {line_num}: '{content}'")
            
        total_invalid = len(empty_labels) + len(punctuation_only_labels)
        print("-" * 40)
        print(f"Total problematic labels found: {total_invalid}")
        
        if total_invalid == 44:
            print("✅ This perfectly accounts for the 44 sample difference!")

    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_path}'.")

# --- Execution ---
find_invalid_labels('C:/DAIHOC/OpenOCR/OpenOCR/vintext/text_recognition_data/text_recognition_data/test_data.txt')