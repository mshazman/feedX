let host = window.location.host;
let questions = null;

function* getNextQuestions(questions) {
    for (let i = 0; i < questions.length; i++) {
        yield questions[i]
    }
}

const loadQuiz = (quiz_id) => {
    document.getElementById("quiz-start").disabled = true;
    fetch(`http://${host}/quiz/api/quiz/${quiz_id}`).then(res => res.json()).then(data => {
        questions = getNextQuestions(data['questions']);
        document.getElementById("quiz-start").disabled = false;
    });
}

const nextQuestion = () => {
    event.preventDefault();
    question = questions.next();
    if (question.done == false) {
        data = question.value;
        fetch(`http://${host}/quiz/template/render/question.html`, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json",
            },
        }).then(res => res.text()).then(result => showQuestion(result));
    } else {
        fetch(`http://${host}/quiz/template/render/thanks.html`).then(res => res.text()).then(result => showQuestion(result));
    }

    answerSubmission()
};

const showQuestion = result => {
    document.querySelector("#participate-main").innerHTML = result;
};

const getFormDict = data => {
    let data_dictionary = {};
    data.forEach(element => {
        data_dictionary[element["name"]] = element["value"];
    });
    return data_dictionary;
};

const answerSubmission = () => {
    event.preventDefault();
    let form = $(".question-form").serializeArray();
    data = getFormDict(form);
    delete data['csrfmiddlewaretoken'];
    delete data['option'];

    if (data['ques_type'] == 1) {
        delete data['ques_type'];
        fetch(`http://${host}/quiz/api/submission`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json",
            },
            body: JSON.stringify(data)
        }).then(response => console.log(response.json()));

    } else {
        delete data['ques_type'];
        let answers = document.getElementsByName("sub_answer");
        answers.forEach(element => {
            if (element.checked) {
                data['sub_answer'] = element.value;
                console.log(data);
                fetch(`http://${host}/quiz/api/submission`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Accept": "application/json",
                    },
                    body: JSON.stringify(data)
                }).then(response => console.log(response.json()));
            }

        });
    }

};