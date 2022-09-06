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
- Go to LAADS DAAC website

![LAADS DAAC website](/LAADSWeb.PNG)

- Select data and submit order

![submit order](/SubmitOrder.PNG)

- Find order and get order's **URL**

![find order](/OpenOrder.PNG)
![copy url](/CopyURL.PNG)

- Get **Token**

![copy token](/CopyTOKEN.PNG)

## Open RSDownloader and enter TOKEN, URL and SAVE PATH information
- Copy and paste **TOKEN**, **URL** and SAVE PATH information to RSDownloader

![enter information](/EnterInformation.png)

Here, you don't need to enter SAVE PATH information, when you click **DOWNLOAD** button, you can select save path.

![save path](/SavePath.png)
![save path selected](/SavePathSelect.png)

-Download and create `config.txt` file
After enter all required information and click **DOWNLOAD** button, the entered information will be automatically saved as `config.txt` file.

![config file](/ConfigFile.png)

- Load `config.txt` file
Click **FILE** button, you can load the saved `config.txt` file.

![load file](/ConfigSelect.png)

You can also create your own config file with different name, but make sure the file is .txt file. Then you can load different config files to download remote sensing products from different orders. Before creating your own config file, please make sure you input token, url and save path information like this format.

![config format](/ConfigContent.png.png)
