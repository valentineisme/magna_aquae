//
//pesquisas
//

function bacia_para_rio() {
    if ($("select#bh").val() == 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográica</option>';
        $("select#rio").html(options);
        $("select#rio").attr('disabled', true);
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramento").html(options);
        $("select#ponto_monitoramento").attr('disabled', true);
        var options = '<option>Selecione primeiro um ponto de monitoramento</option>';
        $("select#coleta").html(options);
        $("select#coleta").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bh").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                }
                $("select#rio").html(options);
                $("select#rio").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function rio_para_ponto() {
    if ($("select#rio").val() == 'selecione') {
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramento").html(options);
        $("select#ponto_monitoramento").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                rio: $("select#rio").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um ponto</option>';
                for (var i = 0; i < data.length; i++) {
                    latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                    options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                }
                $("select#ponto_monitoramento").html(options);
                $("select#ponto_monitoramento").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function ponto_para_coleta() {
    if ($("select#ponto_monitoramento").val() == 'selecione') {
        var options = '<option>Selecione primeiro um ponto</option>';
        $("select#coleta").html(options);
        $("select#coleta").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/imagem/add/',
            data: {
                ponto: $("select#ponto_monitoramento").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var options = '<option value="selecione">Selecione uma coleta</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['data_coleta'] + '</option>';
                }
                $("select#coleta").html(options);
                $("select#coleta").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}


//
//bacia hidrografica
//

function bh_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/bacia-hidrografica/edit/',
        data: {
            bacia: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#nome_bh").attr('value', data[0].fields['nome']);
            $("input#id_bh").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function bh_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}


//
// rio
//

function rio_pesquisar_bacia() {
    if ($("input[name='Bacia Hidrografica']").val() == 'selecione') {
        window.location.href = '/rio/';
    } else {
        $.ajax({
            type: 'POST',
            url: '/rio/',
            data: {
                bh: $("input[name='Bacia Hidrografica']").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var rios = '';
                if (data.length == 0) {
                    rios += '<tr><td>Não há dados cadastrados.</td></tr>';
                } else {
                    var bacia = $('div').find("[data-value='" + $("input[name='Bacia Hidrografica']").val() + "']").text();
                    for (var i = 0; i < data.length; i++) {
                        rios += '<tr> ' +
                            '<td>' + data[i].fields['nome'] + '</td>' +
                            '<td>' + data[i].fields['dimensao'] + '</td>' +
                            '<td id="bacia' + data[i].pk + '">' + bacia + '</td>' +
                            '<td class="collapsing center aligned">' +
                            '<a class="cursorPointer editarRio" onclick="rio_editar(' + data[i].pk + ')">' +
                            '<i class="ui write grey large icon"></i>' +
                            '</a>' +
                            '</td>' +
                            '<td class="collapsing center aligned"> ' +
                            '<a class="cursorPointer excluirRio" onclick="rio_excluir(' + data[i].pk + ')">' +
                            '<i class="ui trash red large icon"></i>' +
                            '</a>' +
                            '</td> ' +
                            '</tr>';
                    }

                }
                $("tbody#tbrio").html(rios);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function rio_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/rio/edit/',
        data: {
            rio_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#nome_rio").attr('value', data[0].fields['nome']);
            $("input#dimensao_rio").attr('value', data[0].fields['dimensao']);
            $("input#bh_rio").attr('value', $("td#bacia" + id).text());
            $("input#id_rio").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function rio_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
// ponto
//

function ponto_pesquisar_rio() {
    if ($("input[name='Rio']").val() == 'selecione') {
        window.location.href = '/ponto/';
    } else {
        $.ajax({
            type: 'POST',
            url: '/ponto/',
            data: {
                ponto: $("input[name='Rio']").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var pontos = '';
                if (data.length == 0) {
                    pontos += '<td><tr>Não há dados cadastrados</tr></td>';
                } else {
                    var rio = $('div').find("[data-value='" + $("input[name='Rio']").val() + "']").text();
                    for (var i = 0; i < data.length; i++) {
                        pontos += '<tr> <td>' + data[i].fields['latitude'] + '</td> <td>' + data[i].fields['longitude'] + '</td> <td>' + rio + '</td> <td class="collapsing center aligned"> <a class="cursorPointer editarPonto" onclick="ponto_editar(' + data[i].pk + ')"> <i class="ui write grey large icon"></i> </a> </td> <td class="collapsing center aligned"> <input type="hidden" id="' + data[i].pk + '"  value="' + data[i] + '"/> <a class="cursorPointer excluirPonto" onclick="ponto_excluir(' + data[i].pk + ')"/> <i class="ui trash red large icon"></i> </a> </td> </tr>';
                    }
                }
                $("tbody#tbpontos").html(pontos);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function ponto_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/ponto/edit/',
        data: {
            ponto_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#ponto_lat").attr('value', data[0].fields['latitude']);
            $("input#ponto_lon").attr('value', data[0].fields['longitude']);
            $("input#ponto_rio").attr('value', $("td#rio" + id).text());
            $("input#id_ponto").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function ponto_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}


//
// coleta
//

function coleta_info(id) {
    $.ajax({
        type: 'GET',
        url: '/coleta/info/',
        data: {
            id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            data = $.parseJSON(data);
            var tab_rio = $("input[name=" + id + "][id=tab_rio]").val();
            var tab_data = $("input[name=" + id + "][id=tab_data]").val();
            var tab_ponto = $("input[name=" + id + "][id=tab_ponto]").val();
            var coleta = '<tr> <td>' + tab_rio + '</td> <td>' + tab_ponto + ' </td> <td>' + tab_data + ' </td> </tr>';
            var sub = '';
            for (var i = 0; i < data.length; i++) {
                sub += '<tr> <td>' + data[i][0] + '</td> <td>' + data[i][1] + '</td> </tr>';
            }
            $("tbody#tbinfo").html(coleta);
            $("tbody#tbsubs").html(sub);

        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function coleta_filtro() {
    if ($("input[name='Rio']").val() == 'selecione') {
        window.location.href = '/coleta/';
    } else {
        $.ajax({
            type: 'POST',
            url: '/coleta/',
            data: {
                rio: $("input[name='Rio']").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var linhas = '';
                if (data.length == 0) {
                    linhas += '<tr><td>Não há dados cadastrados.</td></tr>';
                } else {
                    var rio = $('div').find("[data-value='" + $("input[name='Rio']").val() + "']").text();
                    for (var i = 0; i < data.length; i++) {
                        linhas += '<tr><td>' + rio + '</td><td>' + data[i].fields['ponto_monitoramento'] + '</td><td>' + data[i].fields['data_coleta'] + '</td><td class="collapsing center aligned"><input type="hidden" id="tab_rio" name="' + data[i].pk + '" value="' + rio + '"/> <input type="hidden" id="tab_ponto" name="' + data[i].pk + '" value="' + data[i].fields['ponto_monitoramento'] + '"/> <input type="hidden" id="tab_data" name="' + data[i].pk + '" value="' + data[i].fields['data_coleta'] + '"/><a class="cursorPointer infoColeta" onclick="coleta_info(' + data[i].pk + ');"><i class="ui plus grey large icon"></i></a></td><td class="collapsing center aligned"><a class="cursorPointer excluirColeta" onclick="coleta_excluir(' + data[i].pk + ');"><i class="ui trash red large icon"></i> </a></tr>';
                    }
                }
                $("tbody#tbcoleta").html(linhas);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function coleta_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
//caso
//

function caso_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
//entorno
//

function entorno_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
//imagem
//


function img_bacia_para_rio() {
    if ($("select#bh_pes").val() == 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográica</option>';
        $("select#rio_pes").html(options);
        $("select#rio_pes").attr('disabled', true);
        $("article#div_img").html('');
        $.ajax({
            type: 'POST',
            url: '/imagem/',
            data: {
                rio: "imgs",
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var imgs = '';
                for (var i = 0; i < data.length; i++) {
                    imgs += '<div class="ui card"><div class="image"><img src="/media/' + data[i].fields["imagem"] + '"></div><div class="content"><a class="header">' + data[i].fields["titulo"] + '</a><div class="meta"><span class="date">' + data[i].fields["data_emissao"] + '</span></div></div></div>';
                }
                $("article#div_img").html(imgs);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bh_pes").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                    console.log(options)
                }
                $("select#rio_pes").html(options);
                $("select#rio_pes").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function imagem_pesquisar() {
    $.ajax({
        type: 'POST',
        url: '/imagem/',
        data: {
            rio: $("select[name='rio_pes']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var imgs = '';
            for (var i = 0; i < data.length; i++) {
                imgs += '<div class="ui card"><div class="image"><img src="/media/' + data[i].fields["imagem"] + '"></div><div class="content"><a class="header">' + data[i].fields["titulo"] + '</a><div class="meta"><span class="date">' + data[i].fields["data_emissao"] + '</span></div></div></div>';
            }
            $("article#div_img").html(imgs);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function img_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
// monitoramento
//

var id_cache = '';
function monitoramento_imagem(id) {
    $("input#imagem").attr('value', id);
    $("span#corner" + id).html('<a class="ui left green corner label"><i class="checkmark icon"></i></a>');
    if (id_cache != '') {
        $("span#corner" + id_cache).html('');
    }
    id_cache = id;
}

function monitoramento_entorno(id) {
    $("input#entorno").attr('value', id);
}

function monitoramento_solucao(id) {
    $("input#caso").attr('value', id);

}

function monitoramento_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/ajax/pesquisa/',
        data: {
            caso: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '';
            var risco = data[0].fields['risco'];
            var solucao = data[0].fields['solucao_sugerida'];
            if (risco == 'A') {
                options = '<option value="B">Baixo</option><option value="M">Médio</option><option selected value="A">Alto</option>';
            } else if (risco = 'M') {
                options = '<option value="B">Baixo</option><option selected value="M">Médio</option><option value="A">Alto</option>';
            } else {
                options = '<option selected value="B">Baixo</option><option value="M">Médio</option><option value="A">Alto</option>';
            }
            $("input#caso").attr('value', id);
            $("select#id_risco").html(options);
            $("textarea#id_solucao_sugerida").html(solucao);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });

}

function abrir() {
    $('.modalAdcSol').modal('show');
}