'use strict';

function Quiz (){
    //A Little React Quiz App
    
//setting up variables
const title = "Match The Correct Name To An Image Of A Bird From Your List:"
const [score, setScore] = React.useState(0)
const [question, setQuestion] = React.useState("Welcome!")
const [currentQuestion, setCurrentQuestion] = React.useState(0)
const [answerOptions, setAnswerOptions] = React.useState([{"name":'start quiz', isCorrect:false}])
const [answers, setAnswers] = React.useState(0)
const [showNav, setShowNav] = React.useState(false)


//fetching data from server
React.useEffect(() =>{
    fetch('/quiz-data.api')
    .then(response => response.json())
    .then(data => {
        const questions = data

    //make answer choices
        const ans = []
        for (const option of answerOptions) 
        {
            const a = 
            (<button onClick={() => checkAnswer(option.isCorrect)}>{option.name}</button>)
            ans.push(a)
        }
    setAnswers(ans)
    
    
    //check answer on click
    const checkAnswer = (isCorrect) => {
		if (isCorrect) {
			setScore(score + 1);
        }
        // else{setScore(score)}
        
        //advance to next question
        const nextQuestion = currentQuestion +1;
		if (nextQuestion < questions.length) {
            setQuestion(<img src = {questions[nextQuestion].question}
            alt="It looks like we couldn't find a photo for this bird"></img>);
            setAnswerOptions(questions[nextQuestion].answers);
            setCurrentQuestion(nextQuestion);
        } 
        //end of quiz
        else{
            setCurrentQuestion(nextQuestion)
            setQuestion("Quiz Completed!")
            setAnswerOptions([])
            setShowNav(true)
            const nextQuestion = 10
        }
    };
}
)
},[currentQuestion])


return(
<div classname = "container-fluid">
    <div classname = "row">
        <div classname = "column-6 offset-6">
            <div id = "question-number">Question {currentQuestion}/10</div>
                <div id = "title">{title}</div>
                    <div id = "question">{question}</div>
                        <div id = "answers">{answers}</div>
                            <div id = "score">Your Score is {score}</div>
                        {showNav ? (<div id = "nav">
                    <div><a href = "/bird-list">Return to Birding List</a></div>
                <div><a href = "/">Return to Homepage</a></div>
            </div>):(<div></div>)}
        </div>
    </div>
</div>
)                                  
}
ReactDOM.render(<Quiz />, document.getElementById('quiz'))
