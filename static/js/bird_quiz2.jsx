// 'use strict';

function Quiz (){
//setting up variables
const title = "How Well Do You Know Your Birds?"
const [score, setScore] = React.useState(0)
const [question, setQuestion] = React.useState(0)
const [currentQuestion, setCurrentQuestion] = React.useState(0)
const [answerOptions, setAnswerOptions] = React.useState(0)
// [
//     {
//       "isCorrect": true, 
//       "name": "Hooded Merganser"
//     }, 
//     {
//       "isCorrect": false, 
//       "name": "chickadee"
//     }
//   ], 
const [answers, setAnswers] = React.useState(<div></div>)


//fetching data from server
React.useEffect(() =>{
    fetch('/quiz-data.api')
    .then(response => response.json())
    .then(data => {
        const questions = data
        console.log(questions)
        
    
     //question
    setQuestion(questions[currentQuestion].question);
    //answer choices
    console.log(questions[currentQuestion].answers)
    setAnswerOptions(questions[currentQuestion].answers);
    console.log(answerOptions)
        const ans = []
        for (const option of answerOptions) 
        {
            const a = (<button onClick={() => checkAnswer(option.isCorrect)}>{option.name}</button>)
            ans.push(a)
        }
    setAnswers(ans)
    
    //check answer on click
    const checkAnswer = (isCorrect) => {
		if (isCorrect) {
			setScore(score + 1);
		}
        //theoretically advance to next question
        const nextQuestion = currentQuestion + 1;
		if (nextQuestion < 10) {
            setQuestion(questions[nextQuestion].question);
            setAnswerOptions(questions[nextQuestion].answers);
            setCurrentQuestion(nextQuestion);
        } 
    };
})}
,[]
)


return(
    <div>
        <div id = "question-number">Question {currentQuestion + 1}/10</div>
            <div>{title}</div>
                <div>{question}</div>
            <div>{answers}</div>
        <div>Your Score is {score}</div>
    </div>
)
}
ReactDOM.render(<Quiz />, document.getElementById('quiz'))
