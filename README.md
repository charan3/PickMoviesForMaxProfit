# PickMoviesForMaxProfit

A movie actor wants to make the max. money by picking the right movies in a given year.
Rules:
- Consider that the actor gets a fixed amount of 1 Crore for each movie that he does,
irrespective of the duration of the money.
- Movies have a contract where the actor is not allowed to work on other movies whose
date conflicts with the selected movies date. For example if the actor have selected a movie from 10th Jan to 20th Jan (both dates inclusive) then the actor can’t select any movies which has a start or end date between 10th to 20th Jan.
- Actors are not worried about optimization of ‘less work and more money’. His aim is to get the max. money even if he has to work for all the days of the year.


#### Design a REST API where the actor can submit the data containing the list of movies with movie name, start date and end date and the API should return the total amount that he can make along with the final list of movies to select.

Sample Input:

{
   "movies":[
      {
         "movie_name":"Bala",
         "start_date":"08 Jan 2020",
         "end_date":"28 Jan 2020"
      },
      {
         "movie_name":"Rock",
         "start_date":"20 Jan 2020",
         "end_date":"30 Jan 2020"
      },
      {
         "movie_name":"PolicyMaker",
         "start_date":"29 Jan 2020",
         "end_date":"16 Feb 2020"
      },
      {
         "movie_name":"Brave",
         "start_date":"02 Feb 2020",
         "end_date":"14 Feb 2020"
      },
      {
         "movie_name":"Drive",
         "start_date":"10 Feb 2020",
         "end_date":"18 Feb 2020"
      },
      {
         "movie_name":"Race",
         "start_date":"15 Feb 2020",
         "end_date":"28 Feb 2020"
      }
   ]
}

Sample Output:

{
    "selected_movies": [
        {
            "end_date": "28 Jan 2020",
            "movie_name": "Bala",
            "start_date": "08 Jan 2020"
        },
        {
            "end_date": "14 Feb 2020",
            "movie_name": "Brave",
            "start_date": "02 Feb 2020"
        },
        {
            "end_date": "28 Feb 2020",
            "movie_name": "Race",
            "start_date": "15 Feb 2020"
        }
    ],
    "total_amount": 30000000
}

Postman Download: https://www.postman.com/downloads/
