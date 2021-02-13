
# foursquare_crawler
This crawler is designed to collect information from Foursquare website(www.foursquare.com ).</br>Using Foursquare API.</br> 
# System Requirements
Ubuntu (Version: 16.04). This project haven’t been tested on other platform.
# Pre-request Packages
This crawler is written in Python 3
Other pre-request packages include:
Httplib2(https://pypi.python.org/pypi/httplib2 )
Guess language 0.2(https://pypi.python.org/pypi/guess-language )
* You can run install.sh to install them.    
# Output Format
   This crawler returns a json format profile.</br>
   example format:</br>
   
    {   
           "user info": { 
           "exist": (_1 for yes 0 for no_),
           "user id": "32",
           "imgURL": xxxx(_user icon url_)
           "address": "New York, NY",
           "facebook": "803834",    
           "twitter": "dens", 
           "gender": "m"(_m for male and f for female_),
           },        
           "tips": {     
               "count": 647(_total number of tips_),     
               "tips content": [     
                   { 
                       "category": "Food",     
                       "polarity": 0.049(_sentiment test score_),      
                       "timestamp": "1450378655", 
                       "agreecount": 2
                       "text": "xxxxx",      
                       "len": 148(_length of the text_),      
                       "photo": "y ",      
                       "venue name": "Mimi Cheng's",
                       "venue country": "AU",   
                       "disagreecount": 0
                    }, 
                    ..._other tips_... 
                ] 
           },
           "friends": {
                "count": 25(_total number of friends_),
                "items": [
                    {
                        "id": "101",  
			    "firstName": "xxxx", 
			    "lastName": "xxxx", 
			    "gender": "male"(_or female_),
			    "countryCode": "AU", 
			    "canonicalUrl": "xxxx", 
			    "canonicalPath": "/xxxx", 
			    "photo": {
				    "prefix": "https://fastly.4sqi.net/img/user/", 
			            "suffix": "/xxxx.jpg"
			    }, 
			    "isAnonymous": False(_or True_), 
			    "tips": {"count": 7}, 
			    "lists": {
				    "groups": [
			                {
			        	    "type": "created",
			                    "count": 2, 
			                    "items": []
			        	}
			            ]
			    }, 
			    "homeCity": " Australia", 
			    "bio": "", 
			    "contact": {
				"twitter": "ross", 
			        "facebook": "6523018"
			     }, 
			    "superuser": 1
		      },
		      ..._other friends_... 
	         ]
            }
     } 
    
# Usage
   Run foursq_crawler.py 
   You may change the central ID (the user ID that the crawler begins) and the upper bound (the maximum number of IDs the crawler captures).
