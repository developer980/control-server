const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(function () {
  $("#otp_form").on("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission
    const otp = $("#otp_input").val();

    const route = `http://${window.location.host}/api/auth/otp-check/`;

    const data = await fetch(route, {
      method: "POST",
      body: JSON.stringify({
        otp,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
    });

    const response = await data.json();

    if (response.status === "ok") {
      // Redirect to home page
      window.location.href = response.redirect_url;
    } else {
      alert(`Error: ${response.message}`);
    }
  });
});
