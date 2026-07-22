class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand.sort()
        counter = Counter(hand)
        print(counter)

        for card in hand:
            if counter[card] > 0:
                for new_card in range(card, card + groupSize):
                    if counter[new_card] <= 0:
                        return False
                    counter[new_card] -= 1
        
        return True