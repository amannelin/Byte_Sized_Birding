'use strict';

const Router = ReactRouterDOM.BrowserRouter;
const Route =  ReactRouterDOM.Route;
const Link =  ReactRouterDOM.Link;
const Prompt =  ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

const BirdName = "Canada Goose"


function Title() {
return "How Well Do You Know Your Birds?"
}



function Question(props) {
    return <div>{props.text}</div>
}
function PossibleAnswers(props){

    return <li><button onClick={() => checkAnswer(props.isCorrect)}>{props.name}</button></li>
    

}

function Answers(props) {
    const [answers, setAnswers] = React.useState([])
    const [quest, setQuest] = React.useState([])
    
    React.useEffect(() =>{
        fetch('/quiz-data.api')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const ans = []
            const q = []
            q.push(<Question text = {data[1].question}/>)
            for (const option of data[1].answers) 
            {
                ans.push(
            <PossibleAnswers key = {option.id} name = {option.name} isCorrect = {option.is_correct}/>)
            }
            setAnswers(ans)
            setQuest(q)
            console.log(q)
        })
    
    }, 
    []);

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
//     const checkAnswer = (isCorrect) => {
//     if (isCorrect) {
//         console.log(isCorrect)
//         score = score + 1;
//     }
// }

//     return score
// }

function ScoreBoard(){

    const [score, setScore] = React.useState(0);
    const checkAnswer = (isCorrect) => {
    if (isCorrect) {
        console.log(isCorrect)
        setScore(score + 1);
    }
}
    return <div>Your Score is {score} </div>
}

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
                <ScoreBoard />
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