class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
      
        hour=(hour*30+minutes*0.5)
        minutes=(minutes*6)
        return (min(abs(hour-minutes),360-(abs(hour-minutes))))
        