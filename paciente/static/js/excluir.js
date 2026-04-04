// Confirmação extra antes de excluir
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formExcluir");

    form.addEventListener("submit", function (e) {
        const confirmacao = confirm("Tem certeza que deseja excluir este paciente?");

        if (!confirmacao) {
            e.preventDefault(); // cancela exclusão
        }
    });
});