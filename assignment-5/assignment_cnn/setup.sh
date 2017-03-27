#!/bin/bash

echo "Checking requirements"
problem=`dpkg-query -l \*virtualenv  | grep ii`
if [[ "" == "${problem}" ]]; then
    echo "Required python virtualenv package seems not to be installed."
    read -p "Would you like to install it?? (root privileges required) [Y/n]" response
    response=$(echo "${response}" | tr "[:upper:]" "[:lower:]")
    if [ "${response}" == "y" ] || [ -z $response ]; then
        sudo apt-get update
        read -p "Would you like to use apt or pip for installing it?? (default apt) [apt/pip]" response
        response=$(echo "${response}" | tr "[:upper:]" "[:lower:]")
        if [ "${response}" == "apt" ] || [ -z $response ]; then
            sudo apt-get install python-virtualenv
        else
            sudo pip install virtualenv
        fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
    fi
    echo "End of installation phase"
fi
problem=`dpkg-query -l libpng*-dev  | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library libpng-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y libpng-dev
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi
problem=`dpkg-query -l libjpeg*-dev 2>&1 | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library libjpeg-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y libjpeg-dev
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi

problem=`dpkg-query -l libfreetype6-dev  | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library libfreetype6-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y libfreetype6-dev
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi
problem=`dpkg-query -l python-dev  | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library python-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y python-dev
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi
problem=`dpkg-query -l lib32ncurses*-dev  | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library lib32ncurses5-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y lib32ncurses5-dev
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi
problem=`dpkg-query -l libblas-dev  | grep ii`
if [[ "" == "${problem}" ]]; then
	echo "Required library libblas-dev seems not to be installed."
	read -p "Would you like to install it?? (root privileges required) [Y/n]" response
	if [ "${response}" == "y" ] || [ -z $response ]; then
		sudo apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
	fi
	if [[ "$?" != "0" ]]; then
		echo "Error"
		exit 1
	fi
fi

echo "Creating virtual environment..."
virtualenv .env                  # Create a virtual environment
source .env/bin/activate         # Activate the virtual environment
echo "Checking and installing required python modules"
pip install -r requirements.txt  # Install dependencies
if [[ "$?" != "0" ]]; then
	echo "Error installing required modules for python"
	exit 1
fi
echo "Done"
echo "Downloading necessary dataset files"
if [ ! -d nc17nn/datasets/cifar-10-batches-py ]; then
	cd nc17nn/datasets
	./get_datasets.sh
	echo "Done"
	cd ..

	echo "Compiling Cython modules for neural networks"

	python setup.py build_ext --inplace
	echo "All Done"
	cd ..
fi
echo "Starting ipython notebook (command: 'ipython notebook')"
echo "DO NOT CLOSE THIS SHELL or you will have to start the ipython notebook again"
ipython notebook
