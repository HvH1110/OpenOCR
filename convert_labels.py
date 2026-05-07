import json
import os
import glob

base_dir = r"C:\DAIHOC\OpenOCR\OpenOCR\datasets\Union14M-Benchmarks"

# Search for annotation files
json_files = glob.glob(os.path.join(base_dir, '**', 'annotation.json*'), recursive=True)

print("Writing perfect label.txt files...\n")

for jf in json_files:
    folder = os.path.dirname(jf)
    txt_out = os.path.join(folder, 'label.txt')
    
    count = 0
    with open(jf, 'r', encoding='utf-8') as f_in, open(txt_out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            line = line.strip()
            if not line: 
                continue
            try:
                # Read the exact JSON format from your error log
                data = json.loads(line)
                filename = data["filename"]
                text = data["text"]
                
                # Write it with a TAB character separating them
                f_out.write(f"{filename}\t{text}\n")
                count += 1
            except Exception as e:
                pass
                
    print(f"✅ Wrote {count} clean labels to {txt_out}")

print("\nDone! You are ready.")