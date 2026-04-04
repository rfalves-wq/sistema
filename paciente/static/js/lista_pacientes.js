document.addEventListener("DOMContentLoaded", function () {

    const busca = document.getElementById("busca");
    const tabela = document.getElementById("tabela-pacientes");

    busca.addEventListener("keyup", function () {

        let query = this.value;

        fetch(`/buscar-pacientes/?q=${query}`)
            .then(res => res.json())
            .then(data => {

                tabela.innerHTML = "";

                data.forEach(p => {
                    tabela.innerHTML += `
                        <tr>
                            <td>${p.nome}</td>
                            <td>${p.cpf}</td>
                            <td>
                                <a href="/editar/${p.id}/" class="btn btn-warning btn-sm">Editar</a>
                                <a href="/deletar/${p.id}/" class="btn btn-danger btn-sm">Excluir</a>
                            </td>
                        </tr>
                    `;
                });

            });

    });

});