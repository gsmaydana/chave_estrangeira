$(document).ready(function(){
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cpf_only_numbers').mask('00000000000', {reverse: true});
    $('.celular').mask('(00) 90000-0000');
    $('.telefone').mask('(00) 0000-0000');
    $('.data').mask('00/00/0000');
    $('.ano').mask('0000');

    // Use delegação de eventos para aplicar a máscara
    $(document).on('input', '.dinheiro', function() {
        $(this).mask('#.00', { reverse: true });
    });
    
});