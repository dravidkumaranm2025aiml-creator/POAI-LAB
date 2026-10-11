import os
from pypdf import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_dir):
    reader = PdfReader(input_pdf_path)
    
    experiments = [
        {
            "name": "Ex_1a_Eight_Queens_Problem.pdf",
            "start_page": 15,
            "end_page": 17,
            "title": "Ex 1a: Eight Queens Problem"
        },
        {
            "name": "Ex_1b_Depth_First_Search.pdf",
            "start_page": 18,
            "end_page": 19,
            "title": "Ex 1b: Implementation of Depth First Search"
        },
        {
            "name": "Ex_1c_Minimax_Algorithm.pdf",
            "start_page": 20,
            "end_page": 23,
            "title": "Ex 1c: Implementation of MINIMAX Algorithm"
        },
        {
            "name": "Ex_1d_A_Star_Search_Algorithm.pdf",
            "start_page": 24,
            "end_page": 26,
            "title": "Ex 1d: Implementation of A* Search Algorithm"
        },
        {
            "name": "Ex_2a_Prolog_Knowledge_Representation.pdf",
            "start_page": 27,
            "end_page": 29,
            "title": "Ex 2a: Decision Making and Knowledge Representation (PROLOG)"
        },
        {
            "name": "Ex_2b_Unification_and_Resolution_Algorithm.pdf",
            "start_page": 30,
            "end_page": 33,
            "title": "Ex 2b: Unification and Resolution Algorithm"
        },
        {
            "name": "Ex_2c_Backward_Chaining.pdf",
            "start_page": 34,
            "end_page": 35,
            "title": "Ex 2c: Implementation of Backward Chaining"
        },
        {
            "name": "Ex_2d_Forward_Chaining.pdf",
            "start_page": 36,
            "end_page": 37,
            "title": "Ex 2d: Implementation of Forward Chaining"
        },
        {
            "name": "Ex_3a_Blocks_World_Program.pdf",
            "start_page": 38,
            "end_page": 41,
            "title": "Ex 3a: Implementation of Blocks World Program"
        },
        {
            "name": "Ex_3b_Fuzzy_Inference_System.pdf",
            "start_page": 42,
            "end_page": 44,
            "title": "Ex 3b: Implementation of Fuzzy Inference System"
        },
        {
            "name": "Viva_Questions_with_Answers.pdf",
            "start_page": 45,
            "end_page": 50,
            "title": "Viva Questions with Answers"
        }
    ]
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Total pages in input PDF: {len(reader.pages)}")
    for exp in experiments:
        writer = PdfWriter()
        # Pages in reader are 0-indexed
        for p in range(exp["start_page"] - 1, exp["end_page"]):
            writer.add_page(reader.pages[p])
        
        output_file = os.path.join(output_dir, exp["name"])
        with open(output_file, "wb") as f_out:
            writer.write(f_out)
        
        num_pages = exp["end_page"] - exp["start_page"] + 1
        print(f"Created: {exp['name']} ({num_pages} pages: {exp['start_page']}-{exp['end_page']}) - {exp['title']}")

if __name__ == "__main__":
    split_pdf("POAI-LabManual.pdf", ".")
