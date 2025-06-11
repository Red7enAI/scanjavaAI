# scanjavaAI

This project will scan a directory of java code for OWASP mobile vulnerabilities.

It requires you have Ollama installed locally as well as an ollama LLM of your choice.

This application works well with Android applications whose APK has been decompressed and saved to a directory.   
For that purpose, jadx-gui works well.  

One of the prompts will ask for a character string to look for in file name to begin analysis.  
This is to look for application specific java files.  You will find this feature useful.
