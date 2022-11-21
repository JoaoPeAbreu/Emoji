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
        login = $("#campoLogin").val();
        senha = $("#campoSenha").val();

        var dados = JSON.stringify({ login: login, senha: senha });
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
$(function() { 
    $(document).on("click", "#btIncluirEmoji", function() {
        dcria = $("#campoDcria").val();
        nemo = $("#campoNemo").val();
        repre = $("#campoRepre").val();
        femo = $("#campoFemo").val();
        classi = $("#campoClassi").val();

        var dados = JSON.stringify({ dcria: dcria, nemo: nemo, repre: repre, femo: femo, classi: classi });
        $.ajax({
            url: 'http://localhost:5000/cadastro_emoji',
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
                $("#campoDcria").val("");
                $("#campoNemo").val("");
                $("#campoRepre").val("");
                $("#campoFemo").val("");
                $("#campoclassi").val("");
            } else {
                alert("Erro no cadastro, por favor contate o administrador " + retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("Erro ao contatar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});
$(function () {
    $(document).on("click", "#btAtualizarEmoji", function () {
        id = $("#campoId").val();
        dcria = $("#campoDcria").val();
        nemo = $("#campoNemo").val();
        repre = $("#campoRepre").val();
        femo = $("#campoFemo").val();
        classi = $("#campoClassi").val();
        var dados = JSON.stringify({ id: id, dcria: dcria, nemo: nemo, repre: repre, femo: femo, classi: classi});
        $.ajax({
            url: 'http://localhost:5000/atualizar_emoji/Emoji',
            type: 'PUT',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: emojiAtualizado,
            error: erroAoAtualizar
        });
        function emojiAtualizado(retorno) {
            if (retorno.resultado == "ok") {
                alert("Emoji atualizado com sucesso!");
                sessionStorage.removeItem('emoji_id');
                window.location = "....html"; //colocar depois o html
            } else {
                alert("ERRO na atualização: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoAtualizar(retorno) {
            alert("ERRO ao contactar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
    //var emoji_id = sessionStorage.getItem('emoji_id');
    //$.ajax({
    //    url: 'http://localhost:5000/retornar/Emoji/' + emoji_id,
    //    method: 'GET',
    //    dataType: 'json',
    //    success: exibir_no_form,
    //    error: function () {
    //        alert("erro ao ler dados, verifique o backend");
    //    }
    //});
    // função executada quando tudo dá certo
    //function exibir_no_form(retorno) {
    //    if (retorno.resultado == "ok") {
    //        pessoa = retorno.detalhes;
    //        $("#campoId").val(pessoa.id);
    //        $("#campoNome").val(pessoa.nome);
    //        $("#campoEmail").val(pessoa.email);
    //        $("#campoTelefone").val(pessoa.telefone);
    //    } else {
    //        alert("ERRO: " + retorno.detalhes)
    //    }
    //}
});