import random
import hashlib #to hash the password

class HackerChallenge:
    def __init__(self):
        
        # hint and hash storage
        self.challenges = [
            {
                'name': 'Password Decoder',
                'type': 'hash',
                'solution': 'b10a8db164e0754105b7a99be72e3fe5',  # hash of 'Hello World'
                'hints': [
                    "Hint 1: Password is quite easy!!!",
                    "Hint 2: Think of the most beginner friendly thing",
                    "Hint 3: This word is legit very beginner friendly,the first step!!!",
                    "Final Hint: Look for the most obvious word in coding world"
                ],
                
                'difficulty': 'EASY'
            }
        ]
        self.current_challenge = None
        self.attempts = 0
    
    def start_challenge(self):
        
        """Initialize a random challenge"""
        self.current_challenge = random.choice(self.challenges)
        self.attempts = 0
        print(f" HACKER'S CHALLENGE: {self.current_challenge['name']}")
        
        print("Try to crack the secret!")
    
    def _generate_hint(self):
        
        """Smart hint generator that will provide hints based on number of attempts you make"""
        
        hints = self.current_challenge['hints']
        
        
        if self.attempts <= len(hints):
            return hints[self.attempts - 1]
        
        # If too many attempts, give a more direct hint
        return "Best Hint: The first step you take while learning how to code"
    
    def try_solution(self, user_input):
        
        """Attempt to solve the challenge with smart hinting"""
        self.attempts += 1
        
        # Hash comparison for password challenge
        if self.current_challenge['type'] == 'hash':
            input_hash = hashlib.md5(user_input.encode()).hexdigest()
            
            if input_hash == self.current_challenge['solution']:
                print(f" HACKED Successfully! Solved in {self.attempts} attempts!")
                return True
            
            else:
                # Hint loop
                
                if self.attempts > 3:
                    print(f" FAILED ATTEMPT #{self.attempts}")
                    print(self._generate_hint())
                else:
                    print(f" INCORRECT PASsWORD. Attempt #{self.attempts}")
        
        return False

def main():
    print(" HACKER'S HINT CHALLENGE ")
    
    # Create and start the challenge
    hacker_game = HackerChallenge()
    hacker_game.start_challenge()
    
    # Test multiple attempts with different inputs
    attempts = ['admin', 'hacker', 'password123', 'password']
    
    for attempt in attempts:
        # Stop if challenge is solved
        if hacker_game.try_solution(attempt):
            break

if __name__ == "__main__":
    main()
