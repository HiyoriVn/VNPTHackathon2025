import os

folders = [
"configs",
"data/vector_db",
"src/utils",
"scripts"
]


files = [
"Dockerfile",
"inference.sh",
"requirements.txt",
"README.md",
"src/predict.py",
"src/router.py",
"src/vnpt_api.py",
"src/rag_pipeline.py",
"src/math_pipeline.py",
"src/safety.py",
"src/utils/io.py",
"src/utils/prompt.py"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

for file in files:
    dirpath = os.path.dirname(file)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8"):
            pass

print("Project structure created successfully")