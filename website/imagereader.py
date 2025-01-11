

import os
import google.generativeai as genai

genai.configure(api_key="API _ KEYS _ HERE")


def prep_image(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Diagram")
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    return sample_file

def extract_text_from_image(sample_file, prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([sample_file, prompt])
    return response.text

def upload_screenshot_view(path):

    sample_file=prep_image(path)
    text = extract_text_from_image(sample_file, "who is in this image if there is any equation solve it ")
    print(text)
    return text



def read_image(path):
	return upload_screenshot_view(path)


if __name__=="__main__":
	read_image("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\BIPIN\\PHOTOS\\Screenshot 2024-02-25 234513.png")
    #"C:\Users\bss22\OneDrive\Desktop\Don't Open\BIPIN\PHOTOS\DBMS_PRESENT.pdf"
    # JUST PUT THE PATH OF ANY FILE TO UPLOAD IT ,DAMN!!!!
