# AI23231 - Principles of Artificial Intelligence Lab

This repository contains all laboratory experiments, source code implementations, output execution screenshots, and merged PDF records for **AI23231: Principles of Artificial Intelligence Lab** (Regulation 2023 - Department of Artificial Intelligence and Data Science).

---

## 📁 Repository Structure

```
Poai/
├── code/                                # Source Python scripts for each experiment
│   ├── ex1a.py                          # 8 Queens Problem (Backtracking)
│   ├── ex1b.py                          # Depth First Search (DFS)
│   ├── ex1c.py                          # MINIMAX Algorithm (Tic-Tac-Toe)
│   ├── ex1d.py                          # A* Search Algorithm
│   ├── ex2a.py                          # Prolog Knowledge Representation
│   ├── ex2b.py                          # Unification & Resolution
│   ├── ex2c.py                          # Backward Chaining
│   ├── ex2d.py                          # Forward Chaining
│   ├── ex3a.py                          # Blocks World Problem
│   └── ex3b.py                          # Fuzzy Inference System
├── final_pdfs/                          # 10 Merged Final PDFs (Problem + Output Answer)
│   ├── Ex_1a_Eight_Queens_Problem_Final.pdf
│   ├── Ex_1b_Depth_First_Search_Final.pdf
│   ├── Ex_1c_Minimax_Algorithm_Final.pdf
│   ├── Ex_1d_A_Star_Search_Algorithm_Final.pdf
│   ├── Ex_2a_Prolog_Knowledge_Representation_Final.pdf
│   ├── Ex_2b_Unification_and_Resolution_Algorithm_Final.pdf
│   ├── Ex_2c_Backward_Chaining_Final.pdf
│   ├── Ex_2d_Forward_Chaining_Final.pdf
│   ├── Ex_3a_Blocks_World_Program_Final.pdf
│   └── Ex_3b_Fuzzy_Inference_System_Final.pdf
├── output_screenshots/                  # High-resolution terminal output images
│   ├── Ex_1a_Eight_Queens_Problem - Output.png
│   ├── Ex_1b_Depth_First_Search - Output.png
│   ├── ...
├── split_experiments.py                 # Automated PDF extraction script
├── render_helper.py                     # High-res terminal screenshot renderer
├── generate_all_answers.py              # Script to run all problems & build answer PDFs
├── merge_final_pdfs.py                  # Script to merge problem & answer PDFs
├── POAI-LabManual.pdf                   # Complete original lab manual
└── Viva_Questions_with_Answers.pdf      # Lab Viva Voce Questions & Answers
```

---

## 🧪 Experiments Summary

| Ex No. | Experiment Name | Code File | Output Screenshot | Merged Final PDF |
|:---:|:---|:---:|:---:|:---:|
| **1a** | Eight Queens Problem | [`code/ex1a.py`](code/ex1a.py) | [PNG](output_screenshots/Ex_1a_Eight_Queens_Problem%20-%20Output.png) | [Final PDF](final_pdfs/Ex_1a_Eight_Queens_Problem_Final.pdf) |
| **1b** | Depth First Search (DFS) | [`code/ex1b.py`](code/ex1b.py) | [PNG](output_screenshots/Ex_1b_Depth_First_Search%20-%20Output.png) | [Final PDF](final_pdfs/Ex_1b_Depth_First_Search_Final.pdf) |
| **1c** | MINIMAX Algorithm | [`code/ex1c.py`](code/ex1c.py) | [PNG](output_screenshots/Ex_1c_Minimax_Algorithm%20-%20Output.png) | [Final PDF](final_pdfs/Ex_1c_Minimax_Algorithm_Final.pdf) |
| **1d** | A* Search Algorithm | [`code/ex1d.py`](code/ex1d.py) | [PNG](output_screenshots/Ex_1d_A_Star_Search_Algorithm%20-%20Output.png) | [Final PDF](final_pdfs/Ex_1d_A_Star_Search_Algorithm_Final.pdf) |
| **2a** | Prolog Knowledge Representation | [`code/ex2a.py`](code/ex2a.py) | [PNG](output_screenshots/Ex_2a_Prolog_Knowledge_Representation%20-%20Output.png) | [Final PDF](final_pdfs/Ex_2a_Prolog_Knowledge_Representation_Final.pdf) |
| **2b** | Unification & Resolution | [`code/ex2b.py`](code/ex2b.py) | [PNG](output_screenshots/Ex_2b_Unification_and_Resolution_Algorithm%20-%20Output.png) | [Final PDF](final_pdfs/Ex_2b_Unification_and_Resolution_Algorithm_Final.pdf) |
| **2c** | Backward Chaining | [`code/ex2c.py`](code/ex2c.py) | [PNG](output_screenshots/Ex_2c_Backward_Chaining%20-%20Output.png) | [Final PDF](final_pdfs/Ex_2c_Backward_Chaining_Final.pdf) |
| **2d** | Forward Chaining | [`code/ex2d.py`](code/ex2d.py) | [PNG](output_screenshots/Ex_2d_Forward_Chaining%20-%20Output.png) | [Final PDF](final_pdfs/Ex_2d_Forward_Chaining_Final.pdf) |
| **3a** | Blocks World Program | [`code/ex3a.py`](code/ex3a.py) | [PNG](output_screenshots/Ex_3a_Blocks_World_Program%20-%20Output.png) | [Final PDF](final_pdfs/Ex_3a_Blocks_World_Program_Final.pdf) |
| **3b** | Fuzzy Inference System | [`code/ex3b.py`](code/ex3b.py) | [PNG](output_screenshots/Ex_3b_Fuzzy_Inference_System%20-%20Output.png) | [Final PDF](final_pdfs/Ex_3b_Fuzzy_Inference_System_Final.pdf) |

---

## 🚀 Setup & Execution

### Prerequisites
Install the required Python packages:
```bash
pip install pypdf numpy matplotlib scikit-fuzzy scipy pillow
```

### Running Experiments
Run any experiment individually:
```bash
python code/ex1a.py
```

### Regenerating All Outputs and PDFs
To re-run all experiments, capture screenshots, and regenerate the merged PDFs:
```bash
python generate_all_answers.py
python merge_final_pdfs.py
```
