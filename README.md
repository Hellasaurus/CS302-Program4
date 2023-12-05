# CS302-Program4
Daniel Melancon
CS302-001

# MTG Collection Tracker

I am a Magic: The Gathering (MTG) player. I chose MTG for this project because I enjoy playing the game, and because the game suits itself to many CS projects because a large corpus of data is available for the game. All of the card data is available online, and I have used a small subset of this data to generate accurate cards in my project.

Many Magic: The Gathering players have large collections of cards, and it can be a challenge keeping track of them all. To that end, I have created a collection tracker that supports adding cards to a collection, and creating decks out of those cards. Currently, this is a very simple school project with basic functionality, but there are several avenues for improving this project. Chiefly, a common way of playing the game is through the MTG Arena game. This game generates text logs, which can be read by third-party applications such as [17 Lands](https://www.17lands.com/), which tracks a user's gameplay to provide insights such as a user's winrate with a particular strategy or in a particular gamemode. This information has a variety of uses, such as showing remaining cards in the deck with their probability of being drawn, suggesting plays to the player, or checking published decklists to alert the user to likely plays by the opponent. 

## BST:
* For this program I have implemented a red-black tree in Tree.py. 
* The tree is used in the player class to store the player's decks

## Sources: 

### Decklists:
* Decklists are pulled from mtggoldfish.com:
    * Esper Midrange    by Kazuhiro Suzuki   -https://www.mtggoldfish.com/archetype/standard-esper-midrange-mid#paper
    * Five-color Ramp   by akimasa yamamoto  -https://www.mtggoldfish.com/archetype/standard-domain-mid#paper
    * Azorius Midrange  by Masashiro Kuroda  -https://www.mtggoldfish.com/archetype/standard-azorius-midrange-mid#paper
    * Mono-Red Aggro    by ponumenume        -https://www.mtggoldfish.com/archetype/standard-mono-red-aggro-mid#paper
    * Boros Convoke     by mistia0902        -https://www.mtggoldfish.com/archetype/standard-boros-aggro-mid#paper
    * Gruul Aggro       by YOSHIJI MIYAKURA  -https://www.mtggoldfish.com/archetype/standard-gruul-dinosaurs-mid#paper
 

### Card Data: 
Card data json is pulled from mtgjson.com : https://mtgjson.com/ 

and used under MIT license:
~~~
Copyright © 2018 – Present, Zach Halpern, Eric Lakatos

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
~~~