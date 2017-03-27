Exercise 2: Convolutional Neural Networks (CNNs)

==========================================================================================================
STEP 1: ENVIRONMENT SETUP 
(If you are using the VirtualBox image everything is already working: go to STEP 2)

In order to be able to do these assignments, you must install the required packages.
I made a script called "setup.sh" that you can execute and hopefully everything should
be installed correctly. 

The setup script assumes that you are using ubuntu. I tested it on ubuntu 14.04. 
If something doesn't work (e.a. some packages cannot be installed) it might be that your 
release has different packages. Don't panic, just have a look at the line of the setup script
that fails and tries to install that package manually.
After the required system packages are installed, the script build a virtual environment for python
and install the required dependencies listed in 'requirements.txt'.

If everything went well, you should see the ipython server appearing in your terminal and a localhost
page opened in your browser.
GO TO STEP 3

==========================================================================================================
STEP 2: RUN THE VIRTUAL ENVIRONMENT (If your coming from STEP 1 you don't need to do this)

To run the virtual environment just open a new terminal and execute the 'run.sh' script.
This script starts the virtual environment for python and runs the ipython server.
After you will terminate the ipython server, the virtual environment will be closed too.

==========================================================================================================
STEP 3: DO THE ASSIGNMENTS
The assignment files are "ConvolutionalNeuralNetworks.ipynb" and "mnist.ipynb". You can open and run them
using the web interface of the ipython notebook. 
In these files, you will find the instructions for the assignments. Follow them step by step.

For the "ConvolutionalNeuralNetworks.ipynb" you will have to implement some code in few dependency files:
"nc17nn/layers.py" and "nc17nn/classifiers/cnn.py"

For the "mnist.ipynb" instead, you can modify directly the code opened in the ipython notebook.

For any problem please contact me at j.acquarelli@cs.ru.nl

==========================================================================================================
STEP 4: COLLECT AND SUBMIT YOUR RESULTS

The script "collectSubmission.sh" should create an archive file you can submit using blackboard.
Please check that the script worked correctly. At least the files
- "cnn.py"
- "layers.py"
- "ConvolutionalNeuralNetworks.ipynb"
- "mnist.ipynb

should be present inside the created archive.