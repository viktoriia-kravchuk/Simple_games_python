import os
import re
import string
from graph import Graph, Vertex
import random

def get_words_from_text(text):
    with open(text,'r') as f:
        words = f.read()
        # if song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)
        words = ' '.join(words.split())
        words = words.lower()
        words = words.translate(str.maketrans('','',string.punctuation)) 
    
    all_words = words.split()
    
    return all_words

def make_graph(words):
    g = Graph()
    previous_word = None
    # check word
    # if not in the graph --> add
    # if previous word --> add an edge
    # --> weight+1
    # set current word to previous --> iterate to the end of tetx

    for word in words:
        word_vertex = g.get_vertex(word)
        #print(word_vertex)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        
        previous_word = word_vertex
    
    g.generate_probability_mapping()

    return g

def compose(g,words, length = 50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main():
    # get words
    words = get_words_from_text("texts\hp_sorcerer_stone.txt")
    
    # if artist --> 
    # words =[]
    # for song_file in os.listdir(f'songs/{artist}'):
    #   if song_file == '.DS_Store':
    #       continue
    #   song_words = get_words_from_text(f'songs/{artist}/{song_file}')
    #   words.extend(song_words)

    # make a graph using that words
    g = make_graph(words)
    # get the next word for x number of words
    composition = compose(g, words, 100)
    # show result
    return (' '.join(composition))


if __name__== '__main__':
    print(main())