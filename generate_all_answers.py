import os
import subprocess
from PIL import Image
from render_helper import render_terminal_screenshot

PROBLEMS = [
    {
        "id": "1a",
        "title": "Ex 1a: Eight Queens Problem",
        "script": "code/ex1a.py",
        "pdf_name": "Ex_1a_Eight_Queens_Problem - Answer.pdf",
        "img_name": "Ex_1a_Eight_Queens_Problem - Output.png",
        "extra_img": None
    },
    {
        "id": "1b",
        "title": "Ex 1b: Implementation of Depth First Search",
        "script": "code/ex1b.py",
        "pdf_name": "Ex_1b_Depth_First_Search - Answer.pdf",
        "img_name": "Ex_1b_Depth_First_Search - Output.png",
        "extra_img": None
    },
    {
        "id": "1c",
        "title": "Ex 1c: Implementation of MINIMAX Algorithm",
        "script": "code/ex1c.py",
        "pdf_name": "Ex_1c_Minimax_Algorithm - Answer.pdf",
        "img_name": "Ex_1c_Minimax_Algorithm - Output.png",
        "extra_img": None
    },
    {
        "id": "1d",
        "title": "Ex 1d: Implementation of A* Search Algorithm",
        "script": "code/ex1d.py",
        "pdf_name": "Ex_1d_A_Star_Search_Algorithm - Answer.pdf",
        "img_name": "Ex_1d_A_Star_Search_Algorithm - Output.png",
        "extra_img": None
    },
    {
        "id": "2a",
        "title": "Ex 2a: Decision Making and Knowledge Representation (PROLOG)",
        "script": "code/ex2a.py",
        "pdf_name": "Ex_2a_Prolog_Knowledge_Representation - Answer.pdf",
        "img_name": "Ex_2a_Prolog_Knowledge_Representation - Output.png",
        "extra_img": None
    },
    {
        "id": "2b",
        "title": "Ex 2b: Unification and Resolution Algorithm",
        "script": "code/ex2b.py",
        "pdf_name": "Ex_2b_Unification_and_Resolution_Algorithm - Answer.pdf",
        "img_name": "Ex_2b_Unification_and_Resolution_Algorithm - Output.png",
        "extra_img": None
    },
    {
        "id": "2c",
        "title": "Ex 2c: Implementation of Backward Chaining",
        "script": "code/ex2c.py",
        "pdf_name": "Ex_2c_Backward_Chaining - Answer.pdf",
        "img_name": "Ex_2c_Backward_Chaining - Output.png",
        "extra_img": None
    },
    {
        "id": "2d",
        "title": "Ex 2d: Implementation of Forward Chaining",
        "script": "code/ex2d.py",
        "pdf_name": "Ex_2d_Forward_Chaining - Answer.pdf",
        "img_name": "Ex_2d_Forward_Chaining - Output.png",
        "extra_img": None
    },
    {
        "id": "3a",
        "title": "Ex 3a: Implementation of Blocks World Program",
        "script": "code/ex3a.py",
        "pdf_name": "Ex_3a_Blocks_World_Program - Answer.pdf",
        "img_name": "Ex_3a_Blocks_World_Program - Output.png",
        "extra_img": None
    },
    {
        "id": "3b",
        "title": "Ex 3b: Implementation of Fuzzy Inference System",
        "script": "code/ex3b.py",
        "pdf_name": "Ex_3b_Fuzzy_Inference_System - Answer.pdf",
        "img_name": "Ex_3b_Fuzzy_Inference_System - Output.png",
        "extra_img": "fuzzy_membership_functions.png"
    }
]

def main():
    screenshots_dir = "output_screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("=== Generating Outputs and PDFs for Experiments ===")
    
    for prob in PROBLEMS:
        print(f"\nProcessing: {prob['title']}...")
        cmd_str = f"py {prob['script']}"
        res = subprocess.run(["py", prob['script']], capture_output=True, text=True)
        output_text = res.stdout
        if res.stderr:
            output_text += "\n" + res.stderr
            
        print(f"Output captured ({len(output_text)} chars). Rendering screenshot...")
        
        # Render image
        img = render_terminal_screenshot(
            title=prob['title'],
            command=cmd_str,
            output_text=output_text,
            extra_image_path=prob['extra_img']
        )
        
        # Save PNG screenshot
        img_path = os.path.join(screenshots_dir, prob['img_name'])
        img.save(img_path, format="PNG")
        print(f"Saved Screenshot: {img_path}")
        
        # Save as PDF
        pdf_path = prob['pdf_name']
        img.save(pdf_path, format="PDF", resolution=150.0)
        print(f"Saved Answer PDF: {pdf_path}")

    print("\nAll experiment answer PDFs and screenshot images generated successfully!")

if __name__ == "__main__":
    main()
