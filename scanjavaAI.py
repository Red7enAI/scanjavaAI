
####################################################################################
## Copyright (c) 2025 Red7en, LLC                                                 ##
##                                                                                ## 
## Permission is hereby granted, free of charge, to any person obtaining a copy   ##
## of this software and associated documentation files (the "Software"), to deal  ##
## in the Software without restriction, including without limitation the rights   ##
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      ##
## copies of the Software, and to permit persons to whom the Software is          ##
## furnished to do so, subject to the following conditions:                       ##
##                                                                                ##
## The above copyright notice and this permission notice shall be included in all ##
## copies or substantial portions of the Software.                                ##
##                                                                                ##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     ##   
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       ##
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    ##
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         ##
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  ##
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  ##
## SOFTWARE.                                                                      ##
####################################################################################

import os
import subprocess
import time

def safe_read_file_atomic(path, retries=3, delay=0.2):
    for attempt in range(retries):
        try:
            with open(path, 'r', encoding='latin1') as java_file:
                return java_file.read()
        except UnicodeDecodeError:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

def analyze_java_files(directory):
    """Loop through all Java files in a given directory and analyze them using ollama."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    analysis_dir = os.path.join(directory, "analysis")
    os.makedirs(analysis_dir, exist_ok=True)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java") and file_name_is in file:
                file_path = os.path.join(root, file)
                print (" ")
                print(f"Analyzing: {file_path}")
                
                try:
                    java_code = safe_read_file_atomic(file_path)          
                        
                    result = subprocess.run(
                        ["ollama", "run", "qwen2.5-coder:14b"],
                        input=f"Search for improper credential usage, insecure authentication/authorization, insufficient input/output validation vulnerabilities in this Java file:\n{java_code}",
                        text=True,
                        capture_output=True,
                        encoding='utf-8',
                        errors='replace'
                    )
                    output_file = os.path.join(out_directory, file + ".analysis.txt")
#                 output_file = os.path.join(analysis_dir, file + ".analysis.txt")
                    with open(output_file, "w", encoding="utf-8") as out_file:
                        out_file.write(result.stdout)
                        if "vulnerability" in result.stdout.lower():
                            out_file.write("\n***VULNERABILITY FOUND***\n")
                    
                    print(f"Analysis saved to: {output_file}")
                
                except Exception as e:
                    print(f"Error analyzing {file_path}: {e}")

if __name__ == "__main__":
    print("--------------------------------------------")
    print(" Welcome to scanjavaAI")
    print(" ")    
    java_directory = input("Enter the path to the directory containing Java files: ")
    out_directory = input("Enter the path where analysis files to be written: ")
    file_name_is = input("Enter string to look for in filename for analysis: ")
 
    analyze_java_files(java_directory)

