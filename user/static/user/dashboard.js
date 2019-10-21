jQuery(function($) {
  $("#close-sidebar").click(function() {
    $(".page-wrapper").removeClass("toggled");
  });
  $("#show-sidebar").click(function() {
    $(".page-wrapper").addClass("toggled");
  });
});

// question js

let host = window.location.host;

// dashboard on fetch request
const dashboard = () => {
  fetch(`http://${host}/user/dashboard`)
    .then(res => res.text())
    .then(result => editDashboardMain(result));
};

// helper function for dashboard function
const editDashboardMain = result => {
  let dashboard = document.getElementById("dashboard-content");
  dashboard.innerHTML = result;
};
// create a quiz on dashboard
const createQuiz = filename => {
  fetch(`http://${host}/user/file/${filename}`)
    .then(res => res.text())
    .then(result => editDashboard(result));
};
// add a question on dashboard by removing the previous content
const addQuestion = (quiz_id, filename) => {
  fetch(`http://${host}/quiz/generate_id/`)
    .then(res => res.json())
    .then(result => {
      fetch(`http://${host}/user/file/${filename}/${quiz_id}/${result.id}`)
        .then(res => res.text())
        .then(result => editDashboard(result));
    });
};
// value of checked box in add question
const questionType = () => {
  event.preventDefault();
  id = event.target.id;
  fetch(`http://${host}/quiz/generate_id/`)
    .then(res => res.json())
    .then(result => {
      fetch(`http://${host}/user/file/option.html/${id}/${result.id}`)
        .then(res => res.text())
        .then(result => editOption(result));
    });
};

const editOption = result => {
  document.querySelector("#question-option").innerHTML = result;
};

// refresh the html content of dashboard
const editDashboard = result => {
  document.querySelector("#dashboard-main").innerHTML = result;
};

// data of particular question submit to database
const submitQuestion = () => {
  event.preventDefault();
  let form = $(".question-form").serializeArray();
  let option = document.getElementsByName("option");
  let option_text = document.getElementsByName("option-text");
  data = getFormDict(form);
  question = {
    ques_type: data["question-type"],
    ques_id: data["question-id"],
    ques_text: data["question-Text"],
    quiz: data["quiz-id"]
  };
  question_id = data["question-id"];
  if (option.length > 0 && option_text.length > 0) {
    option_and_answer = getChoiceAndAnswer(question_id, option, option_text);
  }
  console.log(question);
  fetch(`http://${host}/quiz/api/questions/`, {
    method: "POST",
    body: JSON.stringify(question),
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
      Accept: "application/json"
    }
  }).then(res => {
    if (res.ok) {
      choiceSubmission(data["quiz-id"], option_and_answer);
    }
  });
};

// submit choice to the database
const choiceSubmission = (quiz_id, option_and_answer) => {
  let choices = option_and_answer["choice"];
  let answers = option_and_answer["answer"];
  for (i = 0; i < choices.length; i++) {
    data = {
      choice_id: choices[i]["option_id"],
      ques: choices[i]["question_id"],
      choice_text: choices[i]["option_text"]
    };
    console.log(data);

    if (i == choices.length - 1) {
      fetch(`http://${host}/quiz/api/choices/`, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Accept: "application/json"
        }
      }).then(res => {
        if (res.ok) {
          correctAnswerSubmission(quiz_id, answers);
        }
      });
    } else {
      fetch(`http://${host}/quiz/api/choices/`, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Accept: "application/json"
        }
      });
    }
  }
};

// submit answer of a particular question
const correctAnswerSubmission = (quiz_id, answers) => {
  answers.forEach(element => {
    data = {
      ques: element["question_id"],
      answer: element["answer_id"]
    };
    console.log(data);

    fetch(`http://${host}/quiz/api/answers/`, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
        Accept: "application/json"
      }
    });
  });
  addQuestion(quiz_id, "add_question.html");
};
const getChoiceAndAnswer = (question_id, option, option_text) => {
  choice = [];
  answer = [];
  for (i = 0; i < option.length; i++) {
    choice.push({
      question_id: question_id,
      option_id: option[i].value,
      option_text: option_text[i].value
    });
    if (option[i].checked) {
      answer.push({ question_id: question_id, answer_id: option[i].value });
    }
  }

  return { choice: choice, answer: answer };
};
// add a quiz
const quizData = () => {
  event.preventDefault();
  let form = $(".quiz-form").serializeArray();
  data = getFormDict(form);
  console.log(JSON.stringify(data));
  fetch(`http://${host}/quiz/api/quiz/`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json"
    }
  }).then(response =>
    response.json().then(res => {
      console.log(res);
      dashboard();
    })
  );
};

// to submit an answer
const answerSubmission = () => {
  event.preventDefault();
  let form = $(".answer-form").serializeArray();
  data = getFormDict(form);
  console.log(JSON.stringify(data));
  fetch(`http://${host}/quiz/answer/`, {
    method: "POST",
    body: JSON.stringify(data)
  }).then(response => console.log(response.json()));
};

// helperfunction for creating json for post request
const getFormDict = data => {
  let data_dictionary = {};
  data.forEach(element => {
    data_dictionary[element["name"]] = element["value"];
  });
  return data_dictionary;
};

// to fetch all the running/live quizzes that a user can participate in
const liveEvents = () => {
  let myquiz = document.getElementById("my-events");
  let live = document.getElementById("live-events");
  myquiz.style.display = "none";
  live.style.display = "block";
};
// finish adding questions
const getQuizData = id => {
  // Simulate an HTTP redirect:
  var data = {};
  var data = fetch(`http://${host}/quiz/api/quiz/${id}/`).then(response =>
    response
      .json()
      .then(res => {
        console.log(res);
        return res;
      })
      .then(response => {
        finishQuestion(id, response);
      })
  );
};
const finishQuestion = (id, quizinfo) => {
  data = {
    title: quizinfo["title"],
    owner: quizinfo["owner"],
    is_live: true
  };
  fetch(`http://${host}/quiz/api/quiz/${id}/`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
      Accept: "application/json"
    }
  }).then(window.location.replace(`http://${host}/user/dashboard`));
};
// show the details on dashboard page
const showDetails = (quiz_id, filename) => {
  fetch(`http://${host}/user/file/${filename}/${quiz_id}`)
    .then(response => response.text())
    .then(res => {
      var dash = document.getElementById("question");
      console.log(res);
      dash.innerHTML = res;
    });
};

// animate js
