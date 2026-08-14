class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""; answer = []; word_result = [];      
        words_index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,"i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,"y": 24, "z": 25}
        index_words = { 0:"z",1:"y",2:"x",3:"w",4:"v",5:"u",6:"t",7:"s",8:"r",9:"q",10:"p",11:"o",12:"n",13:"m",14:"l",15:"k",16:"j",17:"i",18:"h",19:"g",20:"f",21:"e",22:"d",23:"c",24:"b",25:"a"}
        
        for word in words :
            current_sum = 0
            for i in range(len(word)):
                current = weights[words_index[word[i]]]
                current_sum += current
            answer.append(current_sum)
            
        for num in answer:
            word_result = index_words[num%26]
            result += word_result
        return result