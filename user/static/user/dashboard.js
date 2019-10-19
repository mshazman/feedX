jQuery(function ($) {
  $("#close-sidebar").click(function () {
    $(".page-wrapper").removeClass("toggled");
  });
  $("#show-sidebar").click(function () {
    $(".page-wrapper").addClass("toggled");
  });
});

let host = window.location.host;

// dashboard on fetch request
const dashboard = () => {
  fetch(`http://${host}/user/dashboard`)
    .then(res => res.text())
    .then(result => editDashboardMain(result));
};

// async function dashboard() {
//   let response = await fetch(`http://${host}/user/dashboard`);
//   let data = await response.text();
//   editDashboardMain(data);
// }
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
const addQuestion = filename => {
  quiz_id = event.target.id;
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

// data of particular question
const questionChoice = () => {
  event.preventDefault();
  let form = $(".question-form").serializeArray();
  let option = document.getElementsByName("option");
  let option_text = document.getElementsByName("option-text");
  data = getFormDict(form);
  question_id = data["question-id"];
  console.log(question_id);
  console.log(option);
  console.log(option_text);
  if (option.length > 0 && option_text.length > 0) {
    option_and_answer = getChoiceAndAnswer(question_id, option, option_text);
    console.log(option_and_answer);
  }
  console.log(JSON.stringify(data));
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
  }).then(response => console.log(response.json()));
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
