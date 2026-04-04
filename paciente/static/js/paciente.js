$(document).ready(function(){

    // Máscaras
    $('#id_cpf').mask('000.000.000-00');
    $('#id_telefone').mask('(00) 00000-0000');
    $('#id_telefone_fixo').mask('(00) 0000-0000');
    $('#id_celular').mask('(00) 00000-0000');
    $('#id_cep').mask('00000-000');
    $('#id_rg').mask('00.000.000-0');
    $('#id_cartao_sus').mask('000 0000 0000 0000');
    $('#id_numero').mask('00000');

    // Forçar maiúsculas
    $('input[type="text"], input[type="email"], textarea').on('input', function() {
        this.value = this.value.toUpperCase();
    });

});