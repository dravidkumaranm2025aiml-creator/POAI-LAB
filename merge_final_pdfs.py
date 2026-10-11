import os
from pypdf import PdfReader, PdfWriter

EXPERIMENTS = [
    {
        "normal": "Ex_1a_Eight_Queens_Problem.pdf",
        "ans": "Ex_1a_Eight_Queens_Problem - Answer.pdf",
        "final": "Ex_1a_Eight_Queens_Problem_Final.pdf"
    },
    {
        "normal": "Ex_1b_Depth_First_Search.pdf",
        "ans": "Ex_1b_Depth_First_Search - Answer.pdf",
        "final": "Ex_1b_Depth_First_Search_Final.pdf"
    },
    {
        "normal": "Ex_1c_Minimax_Algorithm.pdf",
        "ans": "Ex_1c_Minimax_Algorithm - Answer.pdf",
        "final": "Ex_1c_Minimax_Algorithm_Final.pdf"
    },
    {
        "normal": "Ex_1d_A_Star_Search_Algorithm.pdf",
        "ans": "Ex_1d_A_Star_Search_Algorithm - Answer.pdf",
        "final": "Ex_1d_A_Star_Search_Algorithm_Final.pdf"
    },
    {
        "normal": "Ex_2a_Prolog_Knowledge_Representation.pdf",
        "ans": "Ex_2a_Prolog_Knowledge_Representation - Answer.pdf",
        "final": "Ex_2a_Prolog_Knowledge_Representation_Final.pdf"
    },
    {
        "normal": "Ex_2b_Unification_and_Resolution_Algorithm.pdf",
        "ans": "Ex_2b_Unification_and_Resolution_Algorithm - Answer.pdf",
        "final": "Ex_2b_Unification_and_Resolution_Algorithm_Final.pdf"
    },
    {
        "normal": "Ex_2c_Backward_Chaining.pdf",
        "ans": "Ex_2c_Backward_Chaining - Answer.pdf",
        "final": "Ex_2c_Backward_Chaining_Final.pdf"
    },
    {
        "normal": "Ex_2d_Forward_Chaining.pdf",
        "ans": "Ex_2d_Forward_Chaining - Answer.pdf",
        "final": "Ex_2d_Forward_Chaining_Final.pdf"
    },
    {
        "normal": "Ex_3a_Blocks_World_Program.pdf",
        "ans": "Ex_3a_Blocks_World_Program - Answer.pdf",
        "final": "Ex_3a_Blocks_World_Program_Final.pdf"
    },
    {
        "normal": "Ex_3b_Fuzzy_Inference_System.pdf",
        "ans": "Ex_3b_Fuzzy_Inference_System - Answer.pdf",
        "final": "Ex_3b_Fuzzy_Inference_System_Final.pdf"
    }
]

def merge_pdfs():
    print("=== Merging Problem and Answer PDFs into 10 Final PDFs ===")
    for item in EXPERIMENTS:
        writer = PdfWriter()
        
        # Add normal PDF pages
        if os.path.exists(item["normal"]):
            reader_normal = PdfReader(item["normal"])
            for page in reader_normal.pages:
                writer.add_page(page)
        else:
            print(f"Warning: {item['normal']} not found!")

        # Add answer PDF pages
        if os.path.exists(item["ans"]):
            reader_ans = PdfReader(item["ans"])
            for page in reader_ans.pages:
                writer.add_page(page)
        else:
            print(f"Warning: {item['ans']} not found!")

        output_path = item["final"]
        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        
        total_p = len(writer.pages)
        print(f"Created: {output_path} (Total {total_p} pages)")

    print("\nSuccessfully merged all 10 Final PDFs!")

if __name__ == "__main__":
    merge_pdfs()
