
# Homework 2: Development of a basic REST-based application 
Author: **Anastasiia Kucheruk**

## How to run the application
1. Clone the repository
2. Open this repository and create new termainla
3. Run the client service using *uvicorn client_service:app --host 127.0.0.1 --port 8000 --reload*
4. Follow link http://127.0.0.1:8000
5. Next, you can go to the http://127.0.0.1:8000/docs for more convenient interaction with the service
6. Try to interact with the service and add your songs

### Results
In this task, I implemented a customer service that interacts with the database and business logic and provides the ability for the client to interact with the songs.
When you click on the link http://127.0.0.1:8000, you will first see the description on the photo:
![alt text](<Знімок екрана 2025-03-28 о 19.35.41.png>)
Then, when you follow the link http://127.0.0.1:8000/docs, you will be able to test all available methods. Let's start from /get. It returns message about this service.
![alt text](<Знімок екрана 2025-03-28 о 19.36.06.png>)
Next, let's try health. It elevates health from a database and a business service and returns the status of both services.
![alt text](<Знімок екрана 2025-03-28 о 19.36.22.png>)
Next, I'll try the post method to add and save a song to the song catalogue. Let's save the song. This is where the service from the database is called.
![alt text](<Знімок екрана 2025-03-28 о 19.37.44.png>)
Next, let's try to retrieve all the songs by calling up the database service. Since I added the song twice, I have two songs on the screenshot.
![alt text](<Знімок екрана 2025-03-28 о 19.38.21-1.png>)
Also, I can get a song by ID, this is also a database service called.
![alt text](<Знімок екрана 2025-03-28 о 19.38.50.png>)
If you enter an ID that is not already in the catalogue, the following message is returned.
![alt text](<Знімок екрана 2025-03-28 о 19.39.00.png>)
There is also a method with recommendations, where a business service is called. Here, open ai is called and there is a default prompt to give a recommendation based on the entered song. 