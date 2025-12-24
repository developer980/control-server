const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(async function () {
  console.log("token:", csrf_token);

  $("#add-user-form").on("submit", async (e) => {
    e.preventDefault();
    const characters =
      "!@#$%^&*()-_=+[{]}|;:',.<>/?`~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const email = $("#email-input").val();
    const firstName = $("#first-name-input").val();
    const lastName = $("#last-name-input").val();
    const route = `http://127.0.0.1:8000/api/c-admin/auth/register/`;
    const password = characters
      .split("")
      .sort(() => 0.5 - Math.random())
      .join("")
      .slice(0, 16);

    console.log(password);

    const data = await fetch(route, {
      method: "POST",
      body: JSON.stringify({
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
    });

    const response = await data.json();
    console.log(response);

    if (response.status === "ok") {
      const message = `<div>A new user has been created with the password:</div>`;
      const message1 = `<div><b>${password}</b></div>`;
      const message2 = `<div>Please make sure to share it with the user as it will not be shown again.</div>`;
      $("#add-user-form").append(message, message1, message2);
    } else {
      alert(`Error: ${response.message}`);
    }
  });
});
