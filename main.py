from PIL import Image
import urllib.request
from http.client import IncompleteRead
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup as soup
import re
from PyQt5.QtWidgets import QMessageBox
import sys
import pyscreenshot as ImageGrab
import pyocr
import pyocr.builders
import webbrowser

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


global page_soup

def a(text):
    replacements = {
        "\n'": "",
        "\r": "",
        "/": "+",
        '"': "+",
        "“": "+",
        "ﬂ": "fi",
        "”": "+",
        "\\": "",
        "ﬁ": "fi",
        ")": "",
        "(": "",
        "‘": "",
    }
    text = "".join([replacements.get(c, c) for c in text])
    return text

def fnd():
    global tag1, tag2, tag3, tag4
    im1 = ImageGrab.grab(bbox=(20, 498 , 241, 612))  # X1,Y1,X2,Y2
    im1.save('a1.png')
    tag1 = tool.image_to_string(
        Image.open('a1.png'),
        lang="deu",
        builder=pyocr.builders.TextBuilder()
    )

    im2 = ImageGrab.grab(bbox=(278, 498 , 499, 612))  # X1,Y1,X2,Y2
    im2.save('a2.png')
    tag2 = tool.image_to_string(
        Image.open('a2.png'),
        lang="deu",
        builder=pyocr.builders.TextBuilder()
    )

    im3 = ImageGrab.grab(bbox=(20, 678, 241, 796 ))  # X1,Y1,X2,Y2
    im3.save('a3.png')
    tag3 = tool.image_to_string(
        Image.open('a3.png'),
        lang="deu",
        builder=pyocr.builders.TextBuilder()
    )

    im4 = ImageGrab.grab(bbox=(278, 678, 499, 796 ))  # X1,Y1,X2,Y2
    im4.save('a4.png')
    tag4 = tool.image_to_string(
        Image.open('a4.png'),
        lang="deu",
        builder=pyocr.builders.TextBuilder()
    )

def g(text):
    replacements = {
        "\n'": "",
        "\r": "",
        "ß": "ss",
        "ä": "a",
        "Ä": "A",
        "ö": "o",
        "Ö": "O",
        "ü": "u",
        "Ü": "U",
        "/": "+",
        '"': "+",
        "“": "+",
        "ﬂ": "fi",
        "”": "+",
        "\\": "",
        " ": "+",
        "ﬁ": "fi",
        ")": "",
        "(": "",
        "‘": "",
    }
    text = "".join([replacements.get(c, c) for c in text])
    return text

def s2(page_soup, tag1, tag2, tag3, tag4):
    firstpage = page_soup.findAll("li",{"class":"b_algo"})
    firstdiv = firstpage[0].findAll("a")
    link = firstdiv[0]["href"]
    global t1
    global t2
    global t3
    global t4
    print(link)
    req = urllib.request.Request(
        link,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
    )

    page = urllib.request.urlopen(req)
    page_html = page.read()
    page_soup = soup(page_html, "html.parser")

    result1 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(g(tag1))), recursive=True)
    t1 =len(result1)

    result2 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(g(tag2))), recursive=True)
    t2 = len(result2)

    result3 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(g(tag3))), recursive=True)
    t3 = len(result3)

    result4 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(g(tag4))), recursive=True)
    t4 = len(result4)
    print("done s2")
class Form(QWidget):
    global tools
    global tool
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    print("Will use lang '%s'" % (lang))





    def __init__(self, parent=None):
        super(Form, self).__init__(parent)



        nameLabel = QLabel("Quizduell Master")
        self.nameLine = QLineEdit()
        self.nameWord1 = QLineEdit()
        self.nameWord2= QLineEdit()
        self.nameWord3 = QLineEdit()
        self.nameWord4 = QLineEdit()
        self.submitButton = QPushButton("Scann")
        self.l_pic = QLabel(self)

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.nameWord1)
        buttonLayout1.addWidget(self.nameWord2)
        buttonLayout1.addWidget(self.nameWord3)
        buttonLayout1.addWidget(self.nameWord4)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.l_pic)

        self.submitButton.clicked.connect(self.submitContact)
        pixmap = QPixmap('test.png')
        self.l_pic.setPixmap(pixmap)


        self.l_pic.resize(390, 220)


        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Quizzduell")



    def submitContact(self):
        find = Thread(target = fnd, )
        find.start()

        self.nameWord1.setText("")
        self.nameWord2.setText("")
        self.nameWord3.setText("")
        self.nameWord4.setText("")
        self.nameLine.setText("")



        # Get IMG
        im = ImageGrab.grab(bbox=(28, 191, 490, 414))  # X1,Y1,X2,Y2
        im.save('test.png')
        txt = tool.image_to_string(
            Image.open('test.png'),
            lang="deu",
            builder=pyocr.builders.TextBuilder()
        )





        self.nameLine.setText(txt)
        pixmap = QPixmap('test.png')
        self.l_pic.setPixmap(pixmap)


        txt = g(txt)
        print(txt)
        my_url = 'https://www.bing.com/search?q=' + txt.replace('\n', '+').replace('\r', '+')
        webbrowser.open(my_url, new=1)
        print(my_url)
        try:
            req = urllib.request.Request(
                my_url,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
                }
            )

            page = urllib.request.urlopen(req)
            page_html = page.read()
                    #HTML Parse

            page_soup = soup(page_html, "html.parser")
            find.join()
            total1 = 0
            total2 = 0
            total3 = 0
            total4 = 0

            thread = Thread(target = s2, args = (page_soup, tag1, tag2, tag3, tag4))
            thread.start()

            result1 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(a(tag1))), recursive=True)
            total1 = total1 + len(result1)

            result2 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(a(tag2))), recursive=True)
            total2 = total2 + len(result2)

            result3 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(a(tag3))), recursive=True)
            total3 = total3 + len(result3)

            result4 = page_soup.body.find_all(string=re.compile('.*{0}.*'.format(a(tag4))), recursive=True)
            total4 = total4 + len(result4)
            print("done counting")
            se = " : "
            self.nameWord1.setText(a(tag1) + se + str(total1))
            self.nameWord2.setText(a(tag2) + se + str(total2))
            self.nameWord3.setText(a(tag3) + se + str(total3))
            self.nameWord4.setText(a(tag4) + se + str(total4))

            thread.join()
            total1 =+ t1
            total2 =+ t2
            total3 =+ t3
            total4 =+ t4

            self.nameWord1.setText(a(tag1) + se + str(total1))
            self.nameWord2.setText(a(tag2) + se + str(total2))
            self.nameWord3.setText(a(tag3) + se + str(total3))
            self.nameWord4.setText(a(tag4) + se + str(total4))


            QMessageBox.about(self, "+Done", "Look")


        except Exception as e:
            print(e)
            print("error")
if __name__ == '__main__':
    import sys


    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(800, 300)
    screen.show()

    sys.exit(app.exec_())
