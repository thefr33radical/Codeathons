
## IOBOT - Onboarding Investors leveraging ML & Blockchain
#### MIT FINRA 19

### Architecture 
<img src="https://github.com/thefr33radical/Codeathons/blob/master/MIT_FINRA_19/IOBot/dataset/IOBoT_arch.png" alt="Architecture" width="640" height="480" border="10" align="center" />

### Demo Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=Eqc7-b9KcIM
" target="_blank"><img src="https://github.com/thefr33radical/Codeathons/blob/master/MIT_FINRA_19/IOBot/dataset/IOBoT_demo.png" 
alt="IOBoT Demo" width="640" height="480" border="10" /></a>

### Summary
* IOBoT aims to solve the challenges involved in Investor Onboarding process.  The present procedure in place is languid - Resulting in poor user experience, Inefficient - Expensive to maintain, Obscure - Hard to audit and ensure compliance and impacts all the stakeholders involved in the process ie  Investors,  Broker Firms and Regulators.
The expectations from IOBoT is to reduce the cost of verification, ensure data is tamper proof which guarantees data integrity, enhance transparency, better ease of use for consumers and lastly creates stickiness. 

*  RedTie service is used to send SMS messages to the users and provide links when and where its necessary. 
Computer Vision is used to recognize user photo and user details. Further verification is done by checking similarity between user face and Photo on ID. The server is hosted in AWS EC2 and AWS rekognition is used for machine learning. This can be easily replaced by custom models.
Plaid is used to connect to users bank account which is used for user net worth assessment, and learning about user transaction history.
Services from North Capitol ae used for User accreditation. 
Ethereum is used for blockchain as a distributed database storage. The entire architecture comprises of modules written python and javascript.


### Run

``` 
 pip install -r requirements.txt
 python app.py "key" "secretkey"
 ```

#### Team Members

* Anton Prakash
* Gowtham Nayak
* Issac
* Sefa
