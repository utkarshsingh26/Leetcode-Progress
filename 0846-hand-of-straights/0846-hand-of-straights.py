class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand.sort()
        count = Counter(hand)

        for card in hand:
            if count[card] > 0:
                for newCard in range(card, card + groupSize):
                    if count[newCard] <= 0:
                        return False
                    count[newCard] -= 1
        
        return True