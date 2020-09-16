

# Lab 8: Quiz

Let's build a quiz using the [Open Trivia DB](https://opentdb.com/api_config.php) Using the code below, construct a GUI for the quiz.
- Show each question and answers with radio buttons
- Allow the user to select answers and go to the previous/next question
- At the end, show the user's score
- (optional) Highlight the correct answer and the incorrect answer the user selected
- (optional) Show controls for picking the quiz parameters (amount, category, difficulty)

https://opentdb.com/api.php?amount=10&category=18&difficulty=easy

```javascript
axios({
  method: 'get',
  url: 'https://opentdb.com/api.php',
  params: {
    amount: 10,
    category: 18,
    difficulty: 'easy'
  }
}).then(response => {
  let questions = response.data.results
  console.log(questions)
})
```


You may want to transform the data from the API into a better format to shuffle the answers.

```javascript
let results = [
    {
        category: "Science: Computers",
        type: "multiple",
        difficulty: "medium",
        question: "What five letter word is the motto of the IBM Computer company?",
        correct_answer: "Think",
        incorrect_answers: [
            "Click",
            "Logic",
            "Pixel"
        ]
    }
]

let results = [
    {
        category: "Science: Computers",
        type: "multiple",
        difficulty: "medium",
        question: "What five letter word is the motto of the IBM Computer company?",
        correct: false,
        answers: [{
                text: "Think",
                correct: true
            }, {
                text: "Click",
                correct: false
            }, {
                text: "Logic",
                correct: false
            }, {
                text: "Pixel",
                correct: false
            }
        ]
    }
]
```