import streamlit as st
import requests

def fetch_repos(username):
    url = f"https://api.github.com/users/lopesdiego12/repos"
    response = requests.get(url)
    return response.json()

st.title("GitHub Repositories Viewer")

username = st.text_input("Enter GitHub username")

if username:
    repos = fetch_repos(username)
    if repos:
        for repo in repos:
            st.subheader(repo['name'])
            st.write(repo['description'])
            st.write(f"Stars: {repo['stargazers_count']} | Forks: {repo['forks_count']}")
            st.write(f"Repo URL: {repo['html_url']}")
            st.write("---")
    else:
        st.write("No repositories found or user does not exist.")
