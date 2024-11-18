import streamlit as st
import random

def user_guess_game():
    st.write("## Guess the Number (User's Turn)")
    
    if 'target' not in st.session_state:
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0

    user_guess = st.number_input('Your guess (1-100):', min_value=1, max_value=100, step=1)
    if st.button('Guess') and st.session_state.attempts < 3:
        st.session_state.attempts += 1
        if user_guess < st.session_state.target:
            st.write('Too low!')
        elif user_guess > st.session_state.target:
            st.write('Too high!')
        else:
            st.write(f'Correct! You guessed in {st.session_state.attempts} tries.')
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
        
        if st.session_state.attempts == 3:
            st.write(f'Sorry, the correct number was {st.session_state.target}. Resetting the game.')
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0

def main():
    st.title('User Guessing Game')
    user_guess_game()

if __name__ == '__main__':
    main()
