(function () {
    function init() {
      const carets = document.querySelectorAll(".caret");
      for (let i = 0; i < carets.length; i++) {
        carets[i].addEventListener("click", function (evt) {
          upvote(carets[i].getAttribute("data-hn"));
        });
      }
    }
  
    function upvote(id) {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
  
      fetch("http://127.0.0.1:8000/upvote", {
        method: "POST",
        body: id,
        headers: { "X-CSRFToken": csrftoken },
        mode: "same-origin",
      }).then(() => {
        location.reload();
      });
    }
  
    init();
  })();