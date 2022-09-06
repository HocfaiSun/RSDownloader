![RSDownloader](/RSDownloaderGUI.png)
# About RSDownloader

**RSDownloader** is a convenient downloader to download remote sensing products (like MODIS products) from LAADS DAAC website. The GUI is designed and written based on **Figma** (design tool) and **Tkinter** (GUI tool). The python code is modified based on python file from LAADS DAAC.

# Features
- Download remote sensing products easily.
- Save the input information automaticlly (config.txt).
- Load the saved information (config.txt) without inputing these information again.
- Can skip the downloaded files and continue downloading new files when download the files again due to some problems, like bad network connections.
- Beautiful GUI design : ).

# How to use it
## Download RSDownloader
If you are good at programming, you can download the source code which is `SourceCode`and modify the code. If you are not good at programming, you can download client version which is `RSDownloader Ver.1.0.zip`.

## Obtain your token and order URL
Go to LAADS DAAC website
![LAADS DAAC website](/LAADSWeb.PNG)
Select data and submit order
![submit order](/SubmitOrder.PNG)
Find order and get order's **URL**
![find order](/OpenOrder.PNG)
![copy url](/CopyURL.PNG)
Get **Token**
![copy token](/CopyTOKEN.PNG)
