const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(function () {
  $("#login-form").on("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission

    const email = $("#email").val();
    const password = $("#password").val();
    const route = `http://127.0.0.1:8000/api/auth/login/`;

    // // Simple validation
    // if (!email || !password) {
    //   alert("Please enter both username and password.");
    //   return;
    // }

    // // Send login data to the server
    const data = await fetch(route, {
      method: "POST",
      body: JSON.stringify({
        email,
        password,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
    });

    console.log(data);
  });
});
