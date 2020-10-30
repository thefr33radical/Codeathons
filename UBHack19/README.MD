# Ploutus : Explainable AI 

<img src ="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/881/347/datas/gallery.jpg" width="640" height="480" />

### Links
* [DEVPOST](https://devpost.com/software/ploutos)
* [REPO](https://github.com/pritch9/UBHacking2019)

* [UBHACK](https://www.ubhacking.com/)

### Summary

```
Built With : 
angular.js, flash, forecasting, gcp, gunicorn, heroku, lime, mongodb, prophet, python, react, scipy, sklearn, statistics, tensorflow, twilio
```
#### Inspiration:
The present challenge in Finance and Investment industry is a lack of cutting edge models that can also be explainable.

#### What it does:
The core of Ploutus is comprised of Forecasting algorithms that can do 3/7/10 day rolling forecasts.
We use Hybrid Models for Forecasting comprising of SARIMA-SVR, CNN-LSTM along with standalone models such as ARIMA, LSTM, ExpSmoothing. Here we can see in the long run Hybrid models reduce RMSE.
Ploutus scrapes data of the company we are looking to invest in. Shows the latest news about the company. Shows the Wiki for the company. Shows the options available for rolling or all at once forecast.
The dashboard contains easier to understand stock data and it acts as a financial investment adviser. The dashboard forecasts given companies stocks and gives you advises on Investing.the dashboard is interactive and features additional features stock based news, recommendations** & risk factor**.
How we built it:
Hosted on Flask and Guicorn at the backend. Frontend uses Angular. ML library from Tensorflow, Sklearn and python stats_models are used.

#### Challenges we ran into:
Time series forecasting are the hardest Supervised ML problems. Data transformation for a forecasting algorithms are very different as each model predicts in rolling forecasts or as a whole.
MultiProcessing to run multiple models simultaneously.
Getting from Unstructured to Structured data.
Accomplishments that we are proud of:
Getting Hybrid Modelling algorithm to deployment which is presently an area of research.
What we learned:
We as a team have done a splendid job with building a dashboard that is user interactive. Though it might look simple to the front it has a lot technical and software aspects that's running it. Nothing is easy to build we have made errors and we worked hard to resolve the errors and in that process we as a team learned a lot.

#### What's next for Ploutos:
We have tons of cool ideas for Ploutos that our users are gonna love and we are 100% sure that we can accomplish it but, due to the time constraints we were unable to fit everything in though we have things ready.A novel method we want to implement is Spatio-Temporal Forecasting ie 3D Forecasts where we consider Spatial aspect with time. In future we want to implement all those ideas that we have and more over take users feedback and suggestions and improve towards the dashboard for their liking.
