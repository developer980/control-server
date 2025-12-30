const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(function () {
  $("#login-form").on("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission

    const email = $("#email").val();
    const password = $("#password").val();
    const route = `http://${window.location.host}/api/auth/login/`;
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

    const response = await data.json();

    if (response.status === "ok") {
      // Redirect to otp page
      window.location.href = response.redirect_url;
    } else {
      alert(`Error: ${response.message}`);
    }
  });
});
