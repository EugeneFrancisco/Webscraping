class eugURL:
    def __init__(self, URL):
        self.URL = URL
    
    
    def check(self, arg):
        self.arg = arg
        URLsuffix = self.URL[len(self.URL)-len(arg):len(self.URL)]
        if URLsuffix == self.arg:
            return True
        return False
    
    
    def suffix(self):#finds suffix of URL. example, "wikipedia.com" returns "com"
        letters = list(self.URL)
        length = len(letters)
        for i in range(length-1, 0, -1):
            if letters[i] == ".":
                return "".join(letters[i+1:length])
                break
        return None
