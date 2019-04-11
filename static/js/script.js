$(document).ready(function () {
    $("#owl-homepage").owlCarousel({

        autoPlay: false, //Set AutoPlay to 3 seconds
        items: 3,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [979, 3],
        navigation: true,
        navigationText: ["voltar", "próximo"],
        autoHeight: false,


    });


    $('.ui.dropdown')
        .dropdown()
    ;

    $('.ui.checkbox')
        .checkbox()
    ;


    var $section = $('section').first();
    $section.find('.panzoom').panzoom({
        $zoomIn: $section.find(".zoom-in"),
        $zoomOut: $section.find(".zoom-out"),
        $zoomRange: $section.find(".zoom-range"),
        $reset: $section.find(".reset")
    });


    $('#range-1').range({
        min: 0,
        max: 100,
        start: 0,
    });

    //bacia
    $("body").on("click", ".adicionarBacia", function () {
        $('.modalAdicionarBacia').modal('show');
    });

    $("body").on("click", ".editarBacia", function () {
        $('.modalEditarBacia').modal('show');
    });

    $("body").on("click", ".excluirBacia", function () {
        $('.modalExcluirBacia').modal('show');
    });

    //rio
    $("body").on("click", ".adicionarRio", function () {
        $('.modalAdicionarRio').modal('show');
    });

    $("body").on("click", ".editarRio", function () {
        $('.modalEditarRio').modal('show');
    });

    $("body").on("click",".editarRio", function(){
        $('.modalEditarRio').modal('show');
    });

    $("body").on("click", ".excluirRio", function () {
        $('.modalExcluirRio').modal('show');
    });

    //ponto
    $("body").on("click", ".adicionarPonto", function () {
        $('.modalAdicionarPonto').modal('show');
    });

    $("body").on("click", ".editarPonto", function () {
        $('.modalEditarPonto').modal('show');
    });

    $("body").on("click", ".excluirPonto", function () {
        $('.modalExcluirPonto').modal('show');
    });

    //coleta
    $("body").on("click", ".adicionarColeta", function () {
        $('.modalAdicionarColeta').modal('show');
    });

    $("body").on("click", ".infoColeta", function () {
        $('.modalInfoColeta').modal('show');
    });

    $("body").on("click", ".excluirColeta", function () {
        $('.modalExcluirColeta').modal('show');
    });

    //ponto
    $("body").on("click", ".adicionarCaso", function () {
        $('.modalAdicionarCaso').modal('show');
    });

    $("body").on("click", ".editarCaso", function () {
        $('.modalEditarCaso').modal('show');
    });

    $("body").on("click", ".excluirCaso", function () {
        $('.modalExcluirCaso').modal('show');
    });

    //entorno
    $("body").on("click", ".adicionarEntorno", function () {
        $('.modalAdicionarEntorno').modal('show');
    });

    $("body").on("click", ".excluirEntorno", function () {
        $('.modalExcluirEntorno').modal('show');
    });

    //cadastro
    $("body").on("click", ".cadastro", function () {
        $('.modalCadastro').modal('show');
    });

    $("body").on("click", ".recuperarSenha", function () {
        $('.modalRecuperarSenha').modal('show');
    });

    //imagem
    $("body").on("click", ".adicionarImagem", function () {
        $('.modalAdicionarImagem').modal('show');
    });

    //conta
    $("body").on("click", ".acessarConta", function () {
        $('.modalAcessarConta').modal('show');
    });

    //monitoramento
    $("body").on("click", ".editarSolucao", function () {
        $('.modalEditarSolucao').modal('show');
    });

    $("body").on("click", ".utilizarSolucao", function () {
        $('.modalUtilizarSolucao').modal('show');
    });

    //img

    $("body").on("click", ".excluirImagem", function () {
        $('.modalExcluirImagem').modal('show');
    });
});