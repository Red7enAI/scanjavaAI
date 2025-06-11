# scanjavaAI

This project will scan a directory of java code for OWASP mobile vulnerabilities.
java code is identified as haveing the extension .java

Ollama is required to be installed locally as well as an ollama supported LLM of your choice.
If you don't have Ollama installed, go to http://ollama.com and follow the instructions.
I have found qwen2.5-coder:14b to give the best results.  However you are free to modify the code to your requirements.

This application works well with Android applications whose APK has been decompressed and saved to its own directory.   
For that purpose, jadx-gui works well.  

One of the prompts will ask for a character string to look for in file name in order to begin analysis.  
This is to look for application specific java files instead of all the system related java files.
Entering * in this field will not work to scan all java files regardless of name.
I hope you will find this feature useful.


