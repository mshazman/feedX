jQuery(function($) {
  $("#close-sidebar").click(function() {
    $(".page-wrapper").removeClass("toggled");
  });
  $("#show-sidebar").click(function() {
    $(".page-wrapper").addClass("toggled");
  });
});

let host = window.location.host;

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
      console.log(result.id);
      fetch(`http://${host}/user/file/${filename}/${quiz_id}/${result.id}`)
        .then(res => res.text())
        .then(result => editDashboard(result));
    });
};

// value of checked box in add question
const questionType = () => {
  event.preventDefault();
  id = event.target.id;
  fetch(`http://${host}/user/file/option.html/${id}`)
    .then(res => res.text())
    .then(result => editOption(result));
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

  data = getFormDict(form);
  console.log(JSON.stringify(data));
  // fetch(`http://${host}/quiz/new/`, {
  //   method: "POST",
  //   body: JSON.stringify(data)
  // }).then(response => console.log(response.json()));
};

// add a quiz
const quizData = () => {
  event.preventDefault();
  let form = $(".quiz-form").serializeArray();
  data = getFormDict(form);
  console.log(JSON.stringify(data));
  fetch(`http://${host}/quiz/new/`, {
    method: "POST",
    body: JSON.stringify(data)
  }).then(response => console.log(response.json()));
};

const getFormDict = data => {
  let data_dictionary = {};
  data.forEach(element => {
    data_dictionary[element["name"]] = element["value"];
  });
  return data_dictionary;
};
