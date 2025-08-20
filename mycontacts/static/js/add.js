$(document).ready(function() {
    // Captura o envio do formulário
    $('#add-contact-form').submit(function(e) {
        e.preventDefault(); // Evita recarregar a página

        let form = $(this);
        let url = form.attr('action');
        let data = form.serialize(); // Serializa os campos do formulário

        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: function(response) {
                // Substitui a lista de contatos pelo HTML retornado
                $('#contacts-container').html($(response).find('#contacts-container').html());

                // Limpa os campos do formulário
                form.trigger('reset');

                // Opcional: foco no primeiro campo
                $('#name').focus();
            },
            error: function(xhr, status, error) {
                alert('Ocorreu um erro ao adicionar o contato.');
                console.log(error);
            }
        });
    });
});

