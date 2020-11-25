'use strict';

const Router = ReactRouterDOM.BrowserRouter;
const Route =  ReactRouterDOM.Route;
const Link =  ReactRouterDOM.Link;
const Prompt =  ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

function Title() {
return "How Well Do You Know Your Birds?"
}



function Question(props) {
    return <div>{props.text}</div>
}
function PossibleAnswers(props){
    const [score, setScore] = React.useState(0);
    const checkAnswer = (isCorrect) => {
    if (isCorrect) {
        console.log(isCorrect)
        setScore(score + 1);
        }
    else{
        console.log(isCorrect)
        setScore(score)
    }
}
console.log(score)
    return (<li><button onClick={() => checkAnswer(props.isCorrect)}>{props.name}</button></li>)
    

}

function Answers(props) {
    const [answers, setAnswers] = React.useState([])
    const [question, setQuestion] = React.useState([])
    const currentQuestion = React.useState(0);

    
    React.useEffect(() =>{
        fetch('/quiz-data.api')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const ans = []
            const q = []
            q.push(
            <Question text = {data[0].question}/>
        )
            for (const option of data[0].answers) 
            {
                ans.push(
            <PossibleAnswers name = {option.name} isCorrect = {option.isCorrect}/>
            )
            }
            setAnswers(ans)
            setQuest(q)
            const nextQuestion = currentQuestion + 1;
            if (nextQuestion < quest.length){
                setCurrentQuestion(nextQuestion);
            }
                else{ <div>Quiz Complete</div>}
         }
        )
    },[]
    )

    return (
        <div>
            <div>
                {quest}
            </div>
            <div>
            <ol>
                {answers}
            </ol>
        </div>
        </div>
    )
}


// function ScoreKeeper(){
//     const [score, setScore] = React.useState(0);
//     const checkAnswer = (is_correct) => {
//     if (isCorrect) {
//         console.log(is_correct)
//         score = score + 1;
//     }
// }

//     return score
// }

// function ScoreBoard(){
// const score = 0

//     return <div>Your Score is {score} </div>
// }

function Quiz() {
    return(
        <div>
            <div>
                <Title />
            </div>
            <div>
                <Question />
            </div>
            <div>
                <Answers />

            </div>   
            <div>
                {/* <ScoreBoard /> */}
            </div>     
        </div>
    )
}


ReactDOM.render(<Quiz />, document.getElementById('quiz'))

// fetch('/something, {
//     method: 'POST',
//     body: Json.stringify(data),
    // 'headers'{'Content-Type': 'application/json'
        // credentials: 'include'}
// }