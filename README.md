### This is the backend repository for Inform Me! https://github.com/ACMHacettepeDevelopers/inform_me_gsc_mobile
### There are some instructions to host this repository, than you can get your hosting url and go to https://github.com/ACMHacettepeDevelopers/inform_me_gsc_mobile to make Inform Me alive!

###  Sorry for the trouble! Please bare with us. We tried our best to keep it simple.  We are students so we can't afford to make this service open to public with our credentials yet.

## INSTRUCTIONS
*  git clone https://github.com/ACMHacettepeDevelopers/inform-me-gsc-backend
* Configurations
   
    * Create a service account from https://cloud.google.com, generate service.json file and fill the service.json with your credentials.

    * We are using https://www.microsoft.com/en-us/bing/apis/bing-news-search-api, we included a key for you but in case you get an error like "something is wrong with news api" you have to generate one. (You can get free trial)
    
* Hosting
    * We first tried to host on google cloud but had a problem related to us, ( not related to the codebase or google cloud we just couldn't manage to host it )
    * You can refer to this tutorial for our simple Flask backend, we put a Dockerfile and if you created a service account on Google, all the configuration files are ready in this step! https://aws.amazon.com/tutorials/serve-a-flask-app/. It is dockerized  accordingly to this tutorial.
      
    * You can check https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service. but you might need to change the ports ib the dockerfile and also in the flask_app.py
    * Congrats on hosting! Now note your hosting url  https://github.com/ACMHacettepeDevelopers/inform_me_gsc_mobile/tree/main to make Inform Me alive


## CODEBASE
* The backend service logic / algorithm is written with python from scratch.
* Uses Flask for the backend layer. 
* Utilizes Google TTS, Google STT and Google Translate client libraries.
* Currently Inform Me is in it's initial development phrase. More to come, stay tuned !
* It is tried to be kept clean as much as possible, but the product is delivered in such a hectic schedule. Will be cleaner later.
