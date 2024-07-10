document.getElementById("registerForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('/register', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error("Error:", data.error);
        } else {
            console.log("Success:", data.message);
            alert(data.message);
        }
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});
