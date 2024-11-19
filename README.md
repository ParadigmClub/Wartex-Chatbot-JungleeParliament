# Custom Chatbot (Junglee Parliament) - Prathamesh Prabhakar
![Untitled design](https://github.com/user-attachments/assets/03601598-9ed8-4e87-8a5a-b8db676717c1)
## Overview

This is a custom chatbot application built with **React + Python** featuring a unique UI with Preset Prompts, Formatted responses with **Bullet Points** and **Bold Styling**.


## Samagri

* React + Vite ✡️
* Tailwind CSS 🎨
* Boxicons
* Python + Flask
* Common Sense
* ChatGPT (Bhagwaan)
* Brains (Not the Brain Rotted Skibidi ones) 🧠
## Libraries

* **Flask** : For the backend
* **Firebase** : For the database
* **Google-Generativeai** : For using Gemini API
* **dotenv** : Loading API keys from .env file
* **os** : File Management
## Environment Variables

To run this project, you will need to add the following environment variables to your **.env** file to be placed in the **server** directory

`FIREBASE_DATABASE_URL`

`GOOGLE_API_KEY`

## How to Set Up Firebase

1. Go to **firebase.google.com** and select **Go to Console** option

   ![1](https://github.com/user-attachments/assets/db5d7456-79c8-4034-bae0-5d79db0269c6)

2. Select **Get Started with a Firebase project**

   ![14](https://github.com/user-attachments/assets/6eb60e5f-de62-4ace-9664-6f0d0d914e85)

3. **Name the project ==> Accept the terms ==> Click Continue**![Untitled design](https://github.com/user-attachments/assets/306ca5c7-0af1-4620-a558-d43d6fde0e2f)


![2](https://github.com/user-attachments/assets/56820520-fd77-4de0-bd13-e6b32525297f)

4. Click on **Create project** and wait for it to initialize the project

   ![3](https://github.com/user-attachments/assets/de215b44-a9aa-4ad5-b1dc-656a26ce1cdc)

5. After creating the project, go to the **left of the screen** and select **Build** and click on **Realtime Database**

   ![4](https://github.com/user-attachments/assets/ad322fff-34f9-4403-89da-d003f52fe3e0)

6. Now click on **Create Database**

   ![5](https://github.com/user-attachments/assets/fe61a636-9049-4f77-bebd-e517ba44d667)

7. Select the nearest region for you and click **Next** *(This cannot be changed afterwards)*

   ![6](https://github.com/user-attachments/assets/44350fb6-bc47-42d9-90e4-a0520df7121b)

8. Start the project in **Test Mode** for now

   ![7](https://github.com/user-attachments/assets/5af430f4-d293-46d7-a998-2c7feb9b17c2)

9. The Database is created

   ![8](https://github.com/user-attachments/assets/aa753b76-ea63-4eab-9d85-1ae0727277f4)

10. To connect it to the code, **Click the Gear Icon** near project overview ==> click on **Project Settings**

![10](https://github.com/user-attachments/assets/d48dbbbe-dbdc-4f61-befe-ad277f560a88)

11. Go into **Service Accounts** and click on **Generate New Private Key**

![11](https://github.com/user-attachments/assets/52ba89d7-64e5-424a-bd75-049727960c75)

12. Click on **Generate key**

![12](https://github.com/user-attachments/assets/11f8601b-357a-4c63-b8b7-f125bf16056c)

13. The key will be downloaded on your computer

![13](https://github.com/user-attachments/assets/8df56fac-7a7d-493c-aa4e-81894f4290ba)

14. Now rename the key to ***credentials.json*** and put it in the **server** directory

15. **Copy the URL** seen on **step 9** and paste in the **.env** file under `FIREBASE_DATABASE_URL`

## Set Up Gemini API
1. Visit **ai.google.dev** amd click on **Get API Key in Google AI Studio**

   ![1](https://github.com/user-attachments/assets/558c7917-9552-41c8-875e-90814bfe1660)

2. Select **Develop in your own enviorment**

   ![2](https://github.com/user-attachments/assets/38358ea7-42d2-454e-b87c-d2479b0f2c13)

3. Agree to the Legal Garbage (They will definitely not steal ur personal info) and click **Continue**

   ![3](https://github.com/user-attachments/assets/7773a9f7-46c7-4c94-83d4-8b893963228c)

4. Click on **Create API key** option

   ![4](https://github.com/user-attachments/assets/82c6e97e-d472-4d98-aa02-6d50b4cbe1c2)

5. Select the project we just created in Firebase here (Check out [How to set up Firebase](#how-to-set-up-firebase))

   ![5](https://github.com/user-attachments/assets/65b7cd32-9759-488e-8bd9-f25d3b4c6d09)

6. Copy the API key and paste it in the `GOOGLE_API_KEY` value of **.env** in **./server**

   ![6](https://github.com/user-attachments/assets/66567b59-a954-4beb-bbe8-2d466ff2714e)


## Installation (For Backend)

* To use the project, first of all run `git clone [project_url]`

```bash
  git clone [project_url]
  cd [project]/server
```

* Now install the required libraries by running

```bash 
    pip install -r requirements.txt
```
**It is recommended to setup an enviorment to ensure there are no version overlapping for the libraries**

## Installation (For Frontend)

* After running `git clone [project_url]`, go into the `[project]/client`

```bash
  cd [project]/client
```

* Now install **TailwindCSS** and boxicons by running the following command

```bash 
    npm install -D tailwindcss postcss autoprefixer
    npm install boxicons
```

## Run the program (Backend)
1. go to **../server**
2. run
```bash 
   python app.py
```

## Run the program (Frontend)
1. go to **../client**
2. run
```bash
   npm run dev
```
    
