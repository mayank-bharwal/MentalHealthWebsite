import React, { useState, useEffect } from 'react';
import axios from 'axios';

const JournalPage = () => {
  const [journalEntry, setJournalEntry] = useState('');
  const [entries, setEntries] = useState([]);

  const fetchJournalEntries = async () => {
    try {
      const response = await axios.get('http://localhost:5000/journal');
      setEntries(response.data.entries);
    } catch (error) {
      console.error('Error fetching journal entries:', error);
    }
  };

  useEffect(() => {
    fetchJournalEntries();
  }, []);

  const handleJournalSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/journal', { content: journalEntry });
      setJournalEntry('');
      fetchJournalEntries();
    } catch (error) {
      console.error('Error submitting journal entry:', error);
    }
  };

  return (
    <div>
      <h2>Journal</h2>
      <form onSubmit={handleJournalSubmit}>
        <textarea
          value={journalEntry}
          onChange={(e) => setJournalEntry(e.target.value)}
        ></textarea>
        <button type="submit">Submit Entry</button>
      </form>
      <div>
        {entries.map((entry, index) => (
          <p key={index}>{entry.content}</p>
        ))}
      </div>
    </div>
  );
};

export default JournalPage;