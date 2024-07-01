def load_vocab(file_path):
    """Loads vocabulary words from a text file."""

    with open(file_path, 'r') as f:
        lines = f.readlines()
        words = sorted(set(line.strip().lower() for line in lines))
    return words

def levenshtein_distance(token1, token2):
    """Calculates the Levenshtein distance between two tokens."""

    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for i in range(len(token1) + 1):
        distances[i][0] = i  # Initialize first column for insertions

    for j in range(len(token2) + 1):
        distances[0][j] = j  # Initialize first row for deletions

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]  # No change, minimum cost
            else:
                insertion = distances[i][j - 1] + 1  # Cost of inserting a character
                deletion = distances[i - 1][j] + 1  # Cost of deleting a character
                replacement = distances[i - 1][j - 1] + 1  # Cost of replacing a character
                distances[i][j] = min(insertion, deletion, replacement)  # Choose minimum cost

    return distances[len(token1)][len(token2)]

import streamlit as st

def main():
    """The main function for the Streamlit app."""

    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word:")

    if st.button("Compute"):
        if not word:
            st.error("Please enter a word to find corrections.")
            return

        vocabs = load_vocab("D:/AIO-Exercise/Module1/Week4/data/vocab.txt")
        #vocabs = load_vocab("./vocab.txt")

        leven_distances = {}
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]

        st.write("Correct word:", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(vocabs)

        col2.write("Distances:")
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()