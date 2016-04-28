# Team 10 - Final Project

## Columbia Density Data Exploration
In this project, we explore the historical data (from now until 6/27/2014) from Application Development Initiative's Density project: http://density.adicu.com/
Aspects of this project include:
- Module to scrape and explore Density's historical data in a readable format.
- Application of the above applied to Dining Hall and Library data
        - Dining Hall Occupancy Forecasting
            - For each semester, assume each day of the week has it's own unique pattern
                - Remove any days with less than 600-1000 total occupants (spring break, thanksgiving, etc)
            - Through User-GUI interaction, choose which dining hall and how many hrs. into future to forecast
            - Gather most up-to-date (<15min lag) data from Density API and train SVR classifier:
                - X ~ historical data of same timerange as up-to-date data, y ~ historical datapt directly after (15min)
            - Predict next point with X ~ current data
                - for multiple predictions, append prediction to X and repeat
        - Library Finals Season Analysis
            - Reccomendation engine for which library will have the least percentage occupancy.
 
Google Slide:
https://docs.google.com/presentation/d/1y8WbdyCzO0mK8M26ygPWX7h4Y7I0EgMnDcF9n9hv0oE/edit?usp=sharing
