<!--
      .o8                                      .o8                        
     "888                                     "888                        
 .oooo888   .ooooo.  oooo    ooo          .oooo888   .ooooo.  oooo    ooo 
d88' `888  d88' `88b  `88b..8P'          d88' `888  d88' `88b  `88.  .8'  
888   888  888   888    Y888'    8888888 888   888  888ooo888   `88..8'   
888   888  888   888  .o8"'88b           888   888  888    .o    `888'    
`Y8bod88P" `Y8bod8P' o88'   888o         `Y8bod88P" `Y8bod8P'     `8'     
-->

# SubDomains Finder Tool 🔎
### What is sDFT?
**sDFT** is a tool written in Python that helps you find all accessible **sub-domains** for specific website. It is **simple** and **fast**.
<br><br>

### How it works?
The tool is very simple. All you have to do is specify **target website**. Then, **sDFT** will try to resolve every **subdomain** of specified website and print all that **resolves with success**.

### Installation
#### Linux
```BASH
sudo apt update
sudo apt install python3 python3-pip git # Install dependencies
git clone https://github.com/dox-dev/SubDomains-Finder-Tool.git # Clone sDFT repository
cd SubDomains-Finder-Tool
python3 -m pip install -r requirements.txt # Install pip dependencies
```

#### Windows
1. Download and install [Python 3](https://www.python.org/downloads/) (make sure to add Python and Pip to your PATH)
2. Download [the sDFT repository](https://github.com/dox-dev/SubDomains-Finder-Tool/archive/refs/heads/main.zip)
3. Extract the zip archive you've downloaded and open the folder in command prompt
4. In command prompt type `python -m pip install -r requirements.txt` to install required pip dependencies
5. After doing this, you can use the tool by typing `python main.py --url="your_targeted_website"`

### Usage
In command prompt type `python main.py --url="your_targeted_website"`, where "your_targeted_website" is a website you want to target.
**Remember!** Use URL without `https://www` (for example: **github.com**)

After that, **sDFT** will print all subdomains that resolves with success

##### Footage:
![](https://i.ibb.co/9cSYBY9/m91m191sahbfasif03.gif)

###### Keep in mind that this tool is in its early development, so there still may be some bugs. Also, the list of subdomains will be gradually updated. Sorry for any inconvenience.
