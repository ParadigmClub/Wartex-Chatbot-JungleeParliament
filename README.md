# Custom Chatbot (Junglee Parliament) - Prathamesh Prabhakar




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

3. **Name the project ==> Accept the terms ==> Click Continue**

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

