# Pokemon Population Model Simulator
This is a Python script originally written by YouTuber [Austin Hourigan](https://twitter.com/arhourigan) of [Game Theory](https://www.youtube.com/user/MatthewPatrick13) and featured on the episode ["Why Starters Are DISAPPEARING! | The SCIENCE of... Pokemon"](https://www.youtube.com/watch?v=OccWmmaCqlE). It simulates a population of Bulbasaur, a popular species of Pokémon, breeding and dying until extinction or some population limit is reached. 

## Background
The point of the script is to support a theory regarding the in-game rarity of so-called "starter" Pokémon, creatures which may only be obtained from a professor at the start of a main-series Pokémon game. Austin proposes that these creatures are being raised in captivity due to their incredibly lopsided male-to-female sex ratios. In the real world, animal populations with this kind of ratio are very susceptible to quick changes in the environment such as installation of outdoor lighting or human expansion into natural habitats. The script offers options for natural development and development with some random human intervention to demonstrate this instability. A full explanation of the script and its significance can be found in the video linked above.

## Usage
python -m pokemon_population_models [args]

## Arguments
-n: The Bulbasaur population propagates with no human intervention  
none: The Bulbasaur population propagates with some random human intervention