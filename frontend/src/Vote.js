import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Vote() {
  const [questions, setQuestions] = useState([]);
  const [choices, setChoices] = useState([]);
  const [selectedChoices, setSelectedChoices] = useState({});

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/getData/')
      .then(response => {
        setQuestions(response.data.question);
        setChoices(response.data.choice);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const handleCheckboxChange = (e, choiceId) => {
    setSelectedChoices({
      ...selectedChoices,
      [choiceId]: e.target.checked
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const selectedChoiceIds = Object.keys(selectedChoices).filter(choiceId => selectedChoices[choiceId]);
    const questionId = e.target.getAttribute('data-question-id');
  
    axios.post(`http://127.0.0.1:8000/${questionId}/vote/`, { choice: selectedChoiceIds })
      .then(response => {
        console.log('Vote submitted successfully', selectedChoiceIds);
        // Fetch updated data from the backend after the vote is submitted
        axios.get('http://127.0.0.1:8000/getData/')
          .then(response => {
            setQuestions(response.data.question);
            setChoices(response.data.choice);
          })
          .catch(error => {
            console.log('Error fetching updated data:', error);
          });
      })
      .catch(error => {
        console.log('Error submitting vote:', error);
      });
  };
  

  return (
    <div>
      <h1>Poll Questions</h1>
      {questions.map(question => (
        <div key={question.id}>
          <h2>{question.question_text}</h2>
          <form onSubmit={handleSubmit} data-question-id={question.id} method="POST"> {/* Use POST method */}
 {/* Add data-question-id attribute */}
            <ul>
              {choices && choices
                .filter(choice => choice.question.id === question.id)
                .map(choice => (
                  <li key={choice.id}>
                    <input
                      type="checkbox"
                      id={`choice-${choice.id}`}
                      name={`choice-${choice.id}`}
                      value={choice.id}
                      onChange={(e) => handleCheckboxChange(e, choice.id)}
                    />
                    <label htmlFor={`choice-${choice.id}`}>
                      {choice.choice_text} - Votes: {choice.votes}
                    </label>
                  </li>
                ))}
            </ul>
            <button type="submit">Submit</button>
          </form>
        </div>
      ))}
    </div>
  );
}

export default Vote;
