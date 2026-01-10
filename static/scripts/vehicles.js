const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(function () {
  $("#vehicles-list #generate-password").on("click", async function (event) {
    const clickedElement = event.target.closest(".table-list-primary-item");

    const elementId = clickedElement.getAttribute("id");

    // const message = `
    // <div class="message">
    //   <div class="message-card flex flex-column flex-column-center gap-16">
    //     <p>
    //       Password generated for this vehicle, please share the credentials with the user.
    //     </p>
    //     <button class="button-primary button-2">
    //       Copy Credentials
    //     </button>
    //     <button class="button-primary button-2">
    //       Close
    //     </button>
    //   </div>
    // </div>
    // `;

    // window.confirm("sometext");

    const characters =
      "!@#$%^&*()-_=+[{]}|;:',.<>/?`~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    const password = characters
      .split("")
      .sort(() => 0.5 - Math.random())
      .join("")
      .slice(0, 16);

    if (
      confirm(
        "A password has been generated for this vehicle. Press OK to copy the credentials and share them with the user."
      )
    ) {
      const route = `http://${window.location.host}/api/c-admin/vehicles/update/`;
      const data = await fetch(route, {
        method: "POST",
        body: JSON.stringify({
          id: elementId,
          password,
        }),
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrf_token,
        },
      });

      const response = await data.json();
      console.log(response);
      navigator.clipboard.writeText(
        `Vehicle ID: ${clickedElement.dataset.type[0]}_${clickedElement
          .getAttribute("id")
          .toString()
          .padStart(4, "0")}, Password: ${password}`
      );
    } else console.log("User pressed Cancel");

    alert("Credentials succesfully copied");
  });
});
