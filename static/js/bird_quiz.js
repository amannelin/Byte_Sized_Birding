'use strict';
const a = React.createElement
const b = React.createElement;
const bird = {name:birdName}
const wrong = {names:["chickadee", "nuthatch", "downy"]}

class BirdToGuess extends React.Component {
    constructor(props) {
        super(props);
        this.state = { guessed : false};
        // this.name = { name: session['birds'][0]['comName']};
    }
    render(){
        if (this.state.guessed){
            return "you guessed the bird correctly!"
        }
        return a ('button', 
            {onClick: () => this.setState({guessed : true})},
            bird.name
        );
    }
}
class WrongGuess extends React.Component {
    constructor(props) {
        super(props);
        this.state = { guessed : false};
    }
    render(){
        if (this.state.guessed){
            return "this is not the bird you are looking for"
        }
        for (name of wrong.names){
            console.log(name);
            return a('button',
            {onClick: () =>  this.setState({guessed : true})},
            name
            );
        }
       
    }
}




const a1 = document.querySelector('#answer_1');
ReactDOM.render(a(BirdToGuess), a1);
const a2 = document.querySelector('#answer_2');
ReactDOM.render(b(WrongGuess), a2);
