document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript sėkmingai įkeltas!");

    // Automatinis darbuotojų skaičiaus atnaujinimas kas 5 sek.
    function updateEmployeeCount() {
        fetch("/api/employee-count")
            .then(response => response.json())
            .then(data => {
                data.forEach(darboviete => {
                    let countElement = document.getElementById(`count-${darboviete.id}`);
                    if (countElement) {
                        countElement.textContent = darboviete.darbuotoju_skaicius;
                    }
                });
            })
            .catch(error => console.error("Klaida atnaujinant darbuotojų skaičių:", error));
    }

    updateEmployeeCount();
    setInterval(updateEmployeeCount, 5000);

    // Patvirtinimo pranešimas prieš ištrinant
    document.querySelectorAll(".btn-danger").forEach(button => {
        button.addEventListener("click", function(event) {
            let confirmDelete = confirm("Ar tikrai norite ištrinti šį įrašą?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

    // Automatinis neaktyvių įrašų paryškinimas ir mygtukų išjungimas
    document.querySelectorAll("tr").forEach(row => {
        let isInactive = row.getAttribute("data-status");
        if (isInactive === "inactive") {
            console.log("Neaktyvus darbuotojas rastas:", row);
            row.style.backgroundColor = "#f8d7da";
            row.style.color = "#721c24";
            row.style.textDecoration = "line-through";

            // Išjungti mygtukus neaktyviems darbuotojams
            row.querySelectorAll(".btn").forEach(button => {
                button.classList.add("disabled");
                button.setAttribute("disabled", "true");
            });
        }
    });
});
