import os

print(os.getcwd())

if not os.path.exists("./htmls"):
    os.mkdir("htmls")

for (name, subdirectories, files) in os.walk("."):
    for file_name in files:
        if os.path.splitext(file_name)[1] == ".ipynb":
            path = os.path.join(name, file_name)
            if not name.endswith(".ipynb_checkpoints"):
                output_path = name.replace("./", "htmls/")
                os.system(f"jupyter nbconvert --to html {path} --output-dir={output_path}")
                print(f"{file_name} --> {output_path}")