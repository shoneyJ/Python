### Task 1: Create a shuffled deck of cards

Each card shows a number from 1 to 10. Each number is in the deck four times for a total of 40 cards. At the
beginning of the game, the deck is shuffled (Hint: Look up Fisher-Yates Shuffle Algorithm) to
make sure it is in a random order. Each player receives a stack of 20 cards from the shuffled deck as their
draw pile. The draw pile is kept face-down in front of the player. Each player also keeps a discard pile (see
"Task 3" for more). Tests:

1. A new deck should contain 40 cards
2. A shuffle function should shuffle a deck Hint: Consider mocking Math.random() or the equivalent of your chosen language


### Task 2: Draw cards
Each turn, both players draw the top card. If there are no more cards in the draw pile, shuffle the discard
pile and use those cards as the new draw pile. Once a player has no cards in either their draw or discard
pile, that player loses. Test: If a player with an empty draw pile tries to draw a card, the discard pile is
shuffled into the draw pile.
