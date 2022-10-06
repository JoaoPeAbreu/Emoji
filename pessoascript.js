$(function() { 
    $(document).on("click", "#btIncluirPessoa", function() {
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();

        var dados = JSON.stringify({ nome: nome, email: email, senha: senha });
        $.ajax({
            url: 'http://localhost:5000/cadastro',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json',
            data: dados, 
            success: pessoaIncluida, 
            error: erroAoIncluir
        });
        function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") {
                alert("Cadastro realizado com sucesso!");
                $("#campoNome").val("");
                $("#campoEmail").val("");
                $("#campoSenha").val("");
            } else {
                alert("Erro no cadastro, por favor contate o administrador " + retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("Erro ao contatar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});
$(function() {
    $(document).on("click", "#btnFazerLogin", function() {
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();

        var dados = JSON.stringify({ email: email, senha: senha });
        $.ajax({
            url: 'http://localhost:5000/fazer_login',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', 
            data: dados, 
            success: loginFeito, 
            error: erroaoLogar
        });
        function loginFeito (retorno) {
            if (retorno.resultado == "ok") {
                alert("Login realizado com sucesso!");
                $("#campoEmail").val("");
                $("#campoSenha").val("");
            } else {
                alert("Erro no login: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroaoLogar (retorno) {
            alert("Erro ao contatar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});