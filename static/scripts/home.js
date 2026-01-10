const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(
  $("#vehicle-login-form").on("submit", async function (e) {
    e.preventDefault();
    vehicleId = $("#vehicleId").val();
    password = $("#password").val();

    const route = `http://${window.location.host}/api/c-admin/vehicles/login/`;

    const data = await fetch(route, {
      method: "POST",
      body: JSON.stringify({
        id: vehicleId,
        password: password,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
    });

    const response = await data.json();

    console.log(response);
  })
);
