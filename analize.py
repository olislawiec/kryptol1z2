from collections import Counter
import string

class Decryptor:

    def __init__(self):
        self.cryptogram_messages = []
        self.len_of_shortest = 0
        self.all_posiible_keys = []
        self.candidates_for_key_at_each_position = []
        self.valid_ascii_as_ints = []
        self.create_valid_ascii_characters()
        
    def print_possible_messages(self):
        for counter, one_message in enumerate(self.cryptogram_messages) :
            print("\nMessage nb ", counter)
            for one_letter_position in range(0, self.len_of_shortest):
                if len(self.candidates_for_key_at_each_position[one_letter_position]) == 1:
                    print(chr(self.my_xor(one_message[one_letter_position], self.candidates_for_key_at_each_position[one_letter_position][0])), end='')
                else:
                    print('{', end='')
                    for one_candidate in self.candidates_for_key_at_each_position[one_letter_position]:
                        print(chr(self.my_xor(one_message[one_letter_position], one_candidate)), end='')
                    print('}', end='')

            
    def create_candidates_for_keys(self):
        for letter_at_position in range(0, self.len_of_shortest):
            self.candidates_for_key_at_each_position.append([])
            for one_possible_key in self.all_possible_keys:
                match_counter = 0
                for one_cryptogram in self.cryptogram_messages:
                    if self.xor_value_key_is_valid_ASCII(one_cryptogram[letter_at_position], one_possible_key):
                        match_counter += 1
                if match_counter == self.nb_of_cryptograms: 
                    self.candidates_for_key_at_each_position[letter_at_position].append(one_possible_key)


    def xor_value_key_is_valid_ASCII(self, value, key):
        if self.my_xor(value, key) in self.valid_ascii_as_ints:
            return True
        else:
            return False
            
            
    def my_xor(self, value, key):
        #value will be a string that has to be converted to int (with base = 2)
        #key will be an int
        value = int(value, 2)
        #print('myxor', value, key, value^key)
        return value^key
        
    def print_candidates(self):
        print(self.candidates_for_key_at_each_position)
        
        
    def create_valid_ascii_characters(self):
        self.valid_ascii_as_ints = [ord(x) for x in (string.ascii_lowercase + string.ascii_uppercase + ' ,.!?')]

    def find_len_of_shortest_cryptogram(self):
        self.len_of_shortest = min([len(one_crypto) for one_crypto in self.cryptogram_messages])


    def create_all_possible_keys(self):
        self.all_possible_keys = [x for x in range(0, 256)]

    def print_when_only_one_candidate(self):
        print([x for x in self.candidates_for_key_at_each_position if len(x) < 3])
        
        
    def read_cryptograms_from_file(self):
        self.cryptogram_messages = []
        with open('208791', 'r') as crypto:
            for line in crypto:
                if ('kryptogram' in line) or len(line) < 2 :
                    continue
                else:
                    self.cryptogram_messages.append(line.replace('\n', '').split())
        self.cryptogram_messages.sort(key = lambda c: len(c))
        self.nb_of_cryptograms = self.get_number_of_cryptograms()


    def get_number_of_cryptograms(self):
        return len(self.cryptogram_messages)
        

def main():

    myDecryptor = Decryptor()
    myDecryptor.read_cryptograms_from_file()
    myDecryptor.find_len_of_shortest_cryptogram()
    myDecryptor.create_all_possible_keys()
    myDecryptor.create_candidates_for_keys()

    myDecryptor.print_possible_messages()
    
main()
    
