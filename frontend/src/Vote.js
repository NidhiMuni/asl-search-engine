import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Vote.css'; // Assuming the styles are saved in Vote.css

function DropdownCheckbox({ question, choices, handleCheckboxChange, selectedChoices }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <h2 onClick={() => setIsOpen(!isOpen)} style={{ cursor: 'pointer', marginBottom: isOpen ? '0' : '1rem' }}>
        {question.question_text}
      </h2>
      {isOpen && (
        <ul style={{ listStyleType: "none", padding: '10px', background: "white", border: "1px solid #ccc", borderRadius: '5px', marginBottom: '1rem' }}>
          {choices.map(choice => (
            <li key={choice.id}>
              <input
                type="checkbox"
                id={`choice-${choice.id}`}
                name={`choice-${choice.id}`}
                value={choice.id}
                onChange={(e) => handleCheckboxChange(e, choice.id)}
                checked={selectedChoices[choice.id] || false}
              />
              <label htmlFor={`choice-${choice.id}`}>
                {choice.choice_text}
              </label>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}


function Vote() {
  const [questions, setQuestions] = useState([]);
  const [choices, setChoices] = useState([]);
  const [selectedChoices, setSelectedChoices] = useState({});
  const [mostVoted, setMostVoted] = useState('');
  const [matchConfidence, setMatchConfidence] = useState('');

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
    const formData = {
        questions: {}
    };

    questions.forEach(question => {
        formData.questions[question.id] = choices
            .filter(choice => choice.question.id === question.id && selectedChoiceIds.includes(choice.id.toString()))
            .map(choice => choice.id);
    });

    axios.post('http://127.0.0.1:8000/vote/', formData)
        .then(response => {
            if (response.data.success) {
                console.log('Vote submitted successfully', selectedChoiceIds);
                setMostVoted(response.data.most_voted);
                setMatchConfidence(response.data.match_confidence);
                
                axios.get('http://127.0.0.1:8000/getData/')
                    .then(response => {
                        setQuestions(response.data.question);
                        setChoices(response.data.choice);
                    })
                    .catch(error => {
                        console.log('Error fetching updated data:', error);
                    });
            } else {
                console.log('Vote submission failed:', response.data.message);
            }
        })
        .catch(error => {
            console.log('Error submitting vote:', error);
        });
  };

  return (
    <div>
      <h1>ASL Search Engine</h1>
      <div className="container">
        <div className="column dropdown-column">
          <form onSubmit={handleSubmit} method="POST" id="voteForm">
            {questions.map(question => (
              <DropdownCheckbox
                key={question.id}
                question={question}
                choices={choices.filter(choice => choice.question.id === question.id)}
                handleCheckboxChange={handleCheckboxChange}
                selectedChoices={selectedChoices}
              />
            ))}
          </form>
        </div>
        <div className="column result-column">
          {/* Button moved above the match input box */}
          <button type="submit" form="voteForm" className="submit-button">Find match</button>
          <div style={{ width: '100%' }}>
            <label htmlFor="Match" style={{ display: 'block', marginBottom: '10px' }}>Match:</label>
            <input 
              type="text" 
              id="match" 
              value={`${mostVoted} ${Math.round(matchConfidence * 100)}% match`}
              readOnly
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Vote;
