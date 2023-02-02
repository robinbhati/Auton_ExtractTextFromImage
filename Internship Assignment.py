#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import libraries
import pytesseract
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('D:\CSE\INTERNSHIP\sample image.jpg')

# Convert image to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(image)


# In[6]:


# Set tessereact path
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Extract text from image
text = pytesseract.image_to_string(image)

# Display text
print(text)


# In[12]:


# Read image
image = cv2.imread('D:\CSE\INTERNSHIP\sample image 2.jpg')

# Extract text from image
text = pytesseract.image_to_string(image)

# Display text
print(text)


# In[ ]:




