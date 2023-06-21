# ChatWhiz

ChatWhiz is a chatbot application powered by the OpenAI ChatGPT API. It allows users to interact with a conversational AI model and get responses to their questions or inputs. This README file provides an overview of the project and instructions for setting it up and deploying it using Docker and Jenkins.

## Table of Contents
- Introduction
- Prerequisites
- Installation
- Usage
- Continuous Integration with Jenkins
- Continuous Deployment with Argo CD
- Conclusion

## Introduction

ChatWhiz is a chatbot application that utilizes the OpenAI ChatGPT API to generate responses to user inputs. It provides a user-friendly interface powered by Gradio, allowing users to have interactive conversations with the chatbot.

The main features of ChatWhiz include:

1) Interactive conversation with the chatbot.
2) Integration with the OpenAI ChatGPT API for generating responses.
3) User-friendly interface created using Gradio.
4) This project aims to demonstrate how to build a chatbot application, set up a development environment, and deploy it using Docker and Jenkins for continuous integration (CI) and continuous deployment (CD).

## Prerequisites
Before getting started with ChatWhiz, ensure you have the following prerequisites:

- An API key from OpenAI to access the ChatGPT API.
- Docker installed on your system.
- Jenkins server up and running.
- Docker Hub account for image storage.
- Argo CD installed and configured on your Kubernetes cluster.

## Installation

Follow these steps to set up and install ChatWhiz:

Clone the ChatWhiz repository to your local machine.
Replace "API_KEY" in the code with your actual OpenAI API key.
Install the required dependencies by running pip install -r requirements.txt.
Usage
To use ChatWhiz, follow these steps:

1) Run the application using python ChatWhiz.py.
2) Access the chatbot interface through your web browser.
3) Enter your message or question, and ChatWhiz will respond accordingly.
4)Continuous Integration with Jenkins
5) ChatWhiz can be integrated with Jenkins for continuous integration (CI). Jenkins allows you to automate the build, testing, and deployment process. The provided Jenkinsfile demonstrates how to set up a Jenkins pipeline for building and packaging the application into a Docker image.

## The Jenkins pipeline includes the following stages:

1) Checkout SCM: Checks out the source code from the Git repository (optional).
2) Build Docker Image: Builds the Docker image for ChatWhiz.
3) Push Docker Image: Pushes the Docker image to Docker Hub for image storage.
4) Updating Kubernetes Files: Updates the Kubernetes deployment file with the new image tag.
5) Push Code to Git: Pushes the code changes back to the Git repository.
6) Trigger CD: Triggers the Continuous Deployment (CD) process using your preferred method (e.g., Argo CD).
Please configure the Jenkinsfile according to your specific setup and requirements.

## Continuous Deployment with Argo CD

To enable continuous deployment (CD) for ChatWhiz, you can use Argo CD. Argo CD is a tool that provides automated deployment capabilities for Kubernetes. It allows you to define and synchronize the desired state of your applications stored in a Git repository.

To deploy ChatWhiz using Argo CD, follow these steps:

Install and configure Argo CD on your Kubernetes cluster by referring to the official documentation.
Set up your Git repository as the source of truth for Argo CD, containing the Kubernetes manifest files for ChatWhiz.


## ChatWhiz Application

<img width="1070" alt="Screenshot 2023-06-06 204432" src="https://github.com/THANUSHKIRAN/ChatWhiz/assets/53527645/7e7df9bd-8588-42fd-a73a-f2f979e53c9d">