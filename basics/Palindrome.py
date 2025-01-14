def IsPalindrome(s):
    """Assumes s is a str
        Returns True if letters in s form a palindrom; False otherwise.
        Non-letters and capitalization are ignored."""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ans isPal(s[1:-1])
    return isPal(toChars(s))
    
                
