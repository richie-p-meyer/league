# League of Legends eSport Betting

### Project Description:
With legilization sweeping the nation, online sports betting is at an all-time high. For most, it is pure gambling - place a bet and hope you win! However, for some it is a business - devising tools and techniques to gain the edge. Unfortunately, sports betting is ridiculously competitive with predictive models and analysts flooding the marketplace. Gaining an edge is difficult! But what about the newly emerging field of eSports - is there easy money to be made? League of Legends is a MOBA eSport that was released in 2009. Over the past decade a strong professional scene has developed. There are currently 9 'Tier 1' leagues across the globe that serve as a path towards the World Championship each year. Big money is involved, with top players signing multi-million dollar contracts. World Championship viewership exceeded that of the World Series and Stanley Cup in 2016. Despite all this, eSports betting is far less common than traditional sports. Is there an opportunity?

### Goals:
1. Determine drivers of result (winning/losing)
2. Create a model that predicts game winners at a high enough rate to make money in eSports betting

### To Reproduce:
1. Clone repo
2. Run 'final_project.ipynb'

### Executive Summary:
-Our model accurately predicts professional matches at 59.4%. It is unclear if that is a high enough accuracy to make money betting.

### Planning:
1. Research professional League scene
2. Determine which leagues can be bet upon
    -Which leagues should I use in my model?
3. Determine which features are drivers of winning/losing
4. Scale Data
5. Feature Engineering
    -Rolling Average
    -Merge with next opponent data
6. Create Baseline
7. Create model

### Data Dictionary:
'gamelength' | Length in minutes
'teamkills' | Kills on opponent
'teamdeaths' | Deaths on team
'firstblood' | First to get a kill
'dragons' | How many dragons killed
'barons' | How many barons killed
'opp_barons' | How many barons opponent killed
'towers' | How many towers destroyed
'opp_towers' | How many of teams towers destroyed by opponent
'inhibitors' | How many inhibitors destroyed
'opp_inhibitors' | How many of teams inhibitors destroyed by opponent
'damagetochampions' | Total damage to enemy champions
'damagetakenperminute' | How much damage team took per minute
'wardsplaced' | How many ward placed on map
'wardskilled' | How many enemy wards killed
'controlwardsbought' | How many wards team bought
'totalgold' | Gold earned throughout game
'gspd' | Gold spent percentage differential (how much gold team used compared to opponent)

### Questions:
1. Does blue_side affect result?
2. Does firstblood affect result?
3. Does gspd affect result?
4. Does barons affect result?
5. Does dragons affect result?
6. Does damagetochampions affect result?
7. Does wardsplaced affect result?
8. Does wardskilled affect result?

### Takeaways:
-This model beats the baseline by a substantial amount with more room for improvement
-It is unclear whether it is possible to use this model to make a million dollars

### Next Steps:
-Add tier 2 leagues
-Add individual stats 
-Add at 15 min mark stats
-Incorporate champion picks
-Incorporate betting odds
-Automate script