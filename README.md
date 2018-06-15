# Quizclash / Quizduell OCR *hack / cheat*

![PREVIEW](https://i.imgur.com/gjhwFrT.jpg  "Preview")

This tool simply detects the text in the Image and querrys the web for the right anwsers. Every time it finds the word on a webpage it counts it. So thats it

## Setup

* You need a tool to share your smartphone screen to our pc. I use [**scrcpy**](https://github.com/Genymobile/scrcpy) , but every other tool should work also.
* To run the programm you need **Python 3**
* The uses the following libaries *install with pip*
  ```
  pip install bs4
  pip install pyscreenshot
  pip install pyocr
  pip install PyQt5
  ```
* you also will need [tesseract-ocr](https://github.com/tesseract-ocr) and [tessdata](https://github.com/tesseract-ocr/tessdata) so tesseract-ocr can detect the texin the images

## How to use

* first run the **src.py** in console with `python src.py` and resize your sreen sharing tool to the size of the created window and locate your tool directly on the window, so screenshots are possible.
![resize](resize.gif  "resize")
* now run **main.py** with `python main.py` in the console and you are ready to go. now the tool will do the work for you. *just click __scann__ every time a new question comes up*
