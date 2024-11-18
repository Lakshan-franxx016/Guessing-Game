import streamlit as st
import random

def machine_guess_game():
    st.write("## Guess the Number (Machine's Turn)")
    
    if 'user_target' not in st.session_state:
        st.session_state.user_target = st.number_input('Number for machine to guess (1-100):', min_value=1, max_value=100, step=1)
        st.session_state.min_val = 1
        st.session_state.max_val = 100
        st.session_state.attempts = 0
    
    if st.session_state.attempts < 3 and st.session_state.user_target:
        guess = random.randint(st.session_state.min_val, st.session_state.max_val)
        st.write(f'Machine guesses: {guess}')
        st.session_state.attempts += 1
        if guess < st.session_state.user_target:
            st.write('Too low!')
            st.session_state.min_val = guess + 1
        elif guess > st.session_state.user_target:
            st.write('Too high!')
            st.session_state.max_val = guess - 1
        else:
            st.write(f'Machine guessed correctly in {st.session_state.attempts} tries!')
            st.session_state.user_target = None
            st.session_state.attempts = 0

        if st.session_state.attempts == 3:
            st.write(f'Machine failed to guess the number {st.session_state.user_target}. Resetting the game.')
            st.session_state.user_target = None
            st.session_state.attempts = 0

def main():
    st.title('Machine Guessing Game')
    machine_guess_game()

if __name__ == '__main__':
    main()
