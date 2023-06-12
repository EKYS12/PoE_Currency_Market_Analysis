# Path of Exile Currency Market Analysis

## Data

The data from this project was gathered from the data dumps of [PoE Ninja](https://poe.ninja/data) and then unzipped and collected into a directory `./leagues/` (which is in the `./.gitignore`). That data is then ran through the script `./utils/currency_file_script.py` to creat the contents of `./data/`.

## Introduction
This project is on the economy of the video game **Path of Exile**, or **PoE**. The economy of PoE is player driven with a large empahsis on trading, to the point where there are players who just play the economy by crafting or flipping. The economy revolves around items called "Currency Orbs" which are crafting items that are consumed on use. The supply for these items come from players playing the game, and getting these items as dropped loot as rewards. The demand for these items come from their utility in the creation of powerful items, the major part of character power and progression. The supply and demand of these various currencies lead to them being frequently traded with one another and forming a robust and active trade market. 

Another important aspect to understand the economies of PoE is leagues. The player base of the game is split into leagues. This project mainly focuses on challenge leagues, but also expands a bit into the standard league. Challenge leagues are temporary leagues, where they have a start and end date, and the start of a league is always a fresh start. Players start with 0 wealth, 0 characters, and 0 progress, and all start from the same point. At the end of a challenge league everything gets migrated over to the permanent Standard league. This is why currency still has value as it gets closer to the end of a challenge league.

Finally this project will focus on the specific currencies dropped by the Conquerors, a set of end game bosses that all have a unique currency orb attached to them. These currencies can only be dropped by them. We evaluate their values by looking at their trade ratios witht the `Chaos Orb`, the currency orb that has become the *defaulted* currency for transactions and market discussion. The value of everything is always compared to it's current relationship with `Chaos Orbs`. **DISCLAIMER** The `Chaos Orb` is a currency just like everything else and is affected by various factors just like every other currency in the game, like drop rates, current popular crafting methods, and other game factors. It is not a stablely valued currency, but everthing in the economy revolves around the relation is has with everything else. 

### Additional Information
[Leagues](https://www.poewiki.net/wiki/League#Challenge_leagues)  
[Currency](https://www.poewiki.net/wiki/Currency)  
[Conquerors](https://www.poewiki.net/wiki/Conquerors)  

## Problem Statement
How well can we predict the last 10 days of a leaugue. By predicting the last few days of a league, players can use that information to inform their trading/investing decisions before the end of a league as they prepare for the items to be transfered over to the standard league.

## EDA
As we look through the values of the currencies through out the various leagues they exist, their values are vary chaotic and don't seem to follow a greater pattern between leagues. The league start values don't really overlap with each other very well in any way, and just appear somewhat random in value. There doesn't seem to be any seasonality, and the value is primarily just correlated with the previous day's value, which is to be expected in a market time series. Surprisingly, even when we look at the Standard League price for the currencies since their creations, there isn't a seasonal pattern either. In standard their values are very rigid and stable, with a small range of change. The large influx of currency being added to the market every 3 or so months doesn't seem to make significant impacts.

## Modeling Methods
As we have to model every league seperately due to the way challenge leagues work, it is best to make as automated of a proccess as possible. Thus we work on building everything into functions as possible. By turning every step of the proccess of getting a dataframe all the way to plotting the training set, testing set, and predictions set on to a graph into a function, we can then make a master function that takes all the other functions as pieces and automates the whole proccess. With that, we can first make a dataframe with all the results from Augmented Dickey Fuller tests, to determine out Differencing (d) values in the Arima Models. From there we can run down each currency-league dataframe and go through the checklist of proccessing the data, splitting the data, referencing the dataframe with the ADF test results for **d**, and then manually grid searching for **p** and **q** using the metric of AIC. Finally once we have all those determined we can plug those in as the hyperparameters for an ARIMA model and get our predictions and plot them and look at their MAE and MSE.

## Results
With this proccess, we get the results for each league in a shotgun approach to see if we can get something decent. Sadly, looking over the various models, we can see predicting the last 10 days of league with basic ARIMA modeling doesn't work out to well. Some MAE and MSEs can be particularly high, and the directions that the predictions can go sometimes end up being the exact opposite of the true values. Over all the proccess, didn't lead to many reliable models. 

## Conclusions 
The models didn't preform very well, that much is evident. Predicting the economy of the game, even for a few currencies, is proving to be quite the challenge, similar to real world markets. We cannot use this proccess to reliably predict the last 10 days for the various *Conqueror's Currencies*. The one currency that came to close being some what predictable was the *Redeemer's Exalted Orb* as it would have low error scores for more leagues than the others, but still would be subject to very wrong models for other leagues.

## Next Steps
Next steps for this project would be to create a dash board that a user can use to select a currency and league and get the results for that league. This, along with some refactoring of the fuctions to take in a *league* arguement could then allow the dash board to work with current league dataset. Integrating the PoE trade API, it would be possible to collect the data of the current league, and then put that data through all the code in this project, and simply attempt to predict the next day's value for a currency.
