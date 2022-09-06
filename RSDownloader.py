from __future__ import (division, print_function, absolute_import, unicode_literals)
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askdirectory, askopenfilename

# import tqdm
import argparse
import os
import os.path
import shutil
import sys

try:
    from StringIO import StringIO   # python2
except ImportError:
    from io import StringIO         # python3
    
USERAGENT = 'tis/download.py_1.0--' + sys.version.replace('\n','').replace('\r','')


def geturl(url, token=None, out=None):
    headers = { 'user-agent' : USERAGENT }
    if not token is None:
        headers['Authorization'] = 'Bearer ' + token
    try:
        import ssl
        CTX = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        if sys.version_info.major == 2:
            import urllib2
            try:
                fh = urllib2.urlopen(urllib2.Request(url, headers=headers), context=CTX)
                if out is None:
                    return fh.read()
                else:
                    shutil.copyfileobj(fh, out)
            except urllib2.HTTPError as e:
                print('HTTP GET error code: %d' % e.code(), file=sys.stderr)
                print('HTTP GET error message: %s' % e.message, file=sys.stderr)
            except urllib2.URLError as e:
                print('Failed to make request: %s' % e.reason, file=sys.stderr)
            return None

        else:
            from urllib.request import urlopen, Request, URLError, HTTPError
            try:
                fh = urlopen(Request(url, headers=headers), context=CTX)
                if out is None:
                    return fh.read().decode('utf-8')
                else:
                    shutil.copyfileobj(fh, out)
            except HTTPError as e:
                print('HTTP GET error code: %d' % e.code(), file=sys.stderr)
                print('HTTP GET error message: %s' % e.message, file=sys.stderr)
            except URLError as e:
                print('Failed to make request: %s' % e.reason, file=sys.stderr)
            return None

    except AttributeError:
        # OS X Python 2 and 3 don't support tlsv1.1+ therefore... curl
        import subprocess
        try:
            args = ['curl', '--fail', '-sS', '-L', '--get', url]
            for (k,v) in headers.items():
                args.extend(['-H', ': '.join([k, v])])
            if out is None:
                # python3's subprocess.check_output returns stdout as a byte string
                result = subprocess.check_output(args)
                return result.decode('utf-8') if isinstance(result, bytes) else result
            else:
                subprocess.call(args, stdout=out)
        except subprocess.CalledProcessError as e:
            print('curl GET error message: %' + (e.message if hasattr(e, 'message') else e.output), file=sys.stderr)
        return None
    
DESC = "This script will recursively download all files if they don't exist from a LAADS URL and stores them to the specified path"


def sync(src, dest, tok):
    '''synchronize src url with dest directory'''
    try:
        import csv
        files = [ f for f in csv.DictReader(StringIO(geturl('%s.csv' % src, tok)), skipinitialspace=True) ]
    except ImportError:
        import json
        files = json.loads(geturl(src + '.json', tok))

    # use os.path since python 2/3 both support it while pathlib is 3.4+
    for f in files:
        # currently we use filesize of 0 to indicate directory
        filesize = int(f['size'])
        path = os.path.join(dest, f['name'])
        url = src + '/' + f['name']
        if filesize == 0:
            try:
                print('creating dir:', path)
                os.mkdir(path)
                sync(src + '/' + f['name'], path, tok)
            except IOError as e:
                print("mkdir `%s': %s" % (e.filename, e.strerror), file=sys.stderr)
                sys.exit(-1)
        else:
            try:
                if not os.path.exists(path):
                    print('downloading: ' , path)
                    with open(path, 'w+b') as fh:
                        geturl(url, tok, fh)
                else:
                    print('skipping: ', path)
            except IOError as e:
                print("open `%s': %s" % (e.filename, e.strerror), file=sys.stderr)
                sys.exit(-1)
    return 0

def _main(SaveDir,URL,Token):

    if not os.path.exists(SaveDir):
        os.makedirs(SaveDir)
    return sync(URL, SaveDir, Token)

def btn1_clicked():
    token = entry0.get()
    url = entry1.get()
    save_path = entry2.get()
    if len(save_path) == 0:
        path = askdirectory()
        path = path.replace('/','\\\\')
        save_path = path
    print(token,url,save_path)
    
    config_file = open('config.txt','w')
    print(token,file=config_file)
    print(url,file=config_file)
    print(save_path,file=config_file)
    config_file.close()
    
    tkinter.messagebox.showinfo(title='Downloading Information', message='Start downloading the files, please do not close the downloader!')
    
    if __name__ == '__main__':
        SaveDir = save_path
        DataURL = url
        Token = token     
            
    tkinter.messagebox.showinfo(title='Downloading Information', message='Finish downlaoding the files.')

def btn2_clicked():
    info = askopenfilename()
    info = info.replace('/','\\\\')
    info_all = []
    with open(info) as f:
        for each_line in f:
            line = each_line.replace('\n','')
            info_all.append(line)
    token = info_all[0]
    url = info_all[1]
    save_path = info_all[2]
    print(token,url,save_path)
    
    tkinter.messagebox.showinfo(title='Downloading Information', message='Start downloading the files, please do not close the downloader.')
    
    if __name__ == '__main__':
        SaveDir = save_path
        DataURL = url
        Token = token       
            
    tkinter.messagebox.showinfo(title='Downloading Information', message='Finish downlaoding the files.')
        
window = Tk()
window.title('Remote Sensing Products Downloader VER.1.0 (by ChrisSun)')

window.geometry("1280x720")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    564.5, 360.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    942.0, 245.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    font = (35),
    highlightthickness = 0)

entry0.place(
    x = 667, y = 208,
    width = 550,
    height = 73)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    942.0, 380.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    font = (35),
    highlightthickness = 0)

entry1.place(
    x = 667, y = 343,
    width = 550,
    height = 73)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    876.5, 515.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    font = (35),
    highlightthickness = 0)

entry2.place(
    x = 667, y = 478,
    width = 419,
    height = 73)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b0.place(
    x = 808, y = 613,
    width = 267,
    height = 75)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b1.place(
    x = 1106, y = 478,
    width = 111,
    height = 75)

window.resizable(False, False)
window.mainloop()
