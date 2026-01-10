const csrf_token = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

$(document).ready(function () {
  $("#add-vehicle-form").on("submit", async function (event) {
    event.preventDefault();
    const name = $("#vehicle-name").val();
    const vehicleType = $("#vehicle-type").val();
    const route = `http://${window.location.host}/api/c-admin/add_vehicle/`;

    const data = await fetch(route, {
      method: "POST",
      body: JSON.stringify({
        type: vehicleType,
        name: name,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
    });

    const response = await data.json();
    console.log(response);

    if (response.status === "ok") {
      const message = `<div>A new ${vehicleType} vehicle has been registered</div>`;

      $("#add-vehicle-form").append(message);
    } else {
      alert(`Error: ${response.message}`);
    }
  });
});
