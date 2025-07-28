##Simple Calculator

A basic Python calculator script that performs addition, subtraction, multiplication, and division.

Usage

Run the calculator locally:

python calculator.py

Docker

Build the Docker image

docker build -t simple-calculator .

Run the Docker container

docker run --rm simple-calculator

Save the Docker image to a tar file

docker save -o simple-calculator.tar simple-calculator

Share the Docker image

Send the `simple-calculator.tar` file to someone else.  
They can load it with:

docker load -i simple-calculator.tar
