import React from 'react';
import SearchBar from '../components/SearchBar';

const Home = () => {
    return (
        <div>
            <h1>Welcome to the RAG System</h1>
            <p>Ask your questions below:</p>
            <SearchBar />
        </div>
    );
};

export default Home;