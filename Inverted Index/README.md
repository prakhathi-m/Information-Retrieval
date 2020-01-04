# Information-Retrieval
### Goal:
* To Collect, tokenize, index and query the twitter data.
* To index a reasonable volume of tweets and perform rudimentary data analysis on the collected data.

### Challenges:
*	Setting up an AWS account and creating a EC2 instances.
*	Figuring out the Twitter personalities who hold significant influence on their followers and write script to retrieve replies from their tweets.
*	Correctly setting up the Solr instance to accommodate language and Twitter specific requirements.
*	Finding ways to handle emoticons, dates and coordinates, if present in tweets.
*	Retrieving tweets and replies from user timeline and Searching using hashtags.
*	Getting familiar with Schema files, filters and analyzers of Solr.
*	Crawling 33,000 tweets with various requirements includes:
    *	At least 33,000 tweets in total with not more than 15% being retweets.
    *	At least 1000 tweets per person of interest. 
    * At least 20 replies to each of the tweet posted by the POIs for 5 consecutive days.
    *	At least 3000 replies in total across all POIs
    *	At least 5,000 tweets per language i.e, English, Hindi and Portuguese
    *	At least 5,000 tweets per country
    *	At least 1000 tweets containing hashtags/keywords related to person of interest
    * At least 15 persons of interest (must be a Politicians,Journalists or Social Activists), 5 from each country (USA, India, Brazil) 

