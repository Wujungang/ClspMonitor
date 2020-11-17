function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function(){
    var $a = $('.edit');
    var $add = $('.addtype');
    var $pop = $('.pop_con');
    var $pop_delete = $('#delete_con');
    var $cancel = $('.cancel');
    var $confirm = $('.confirm');
    var $error = $('.error_tip');
    var $input = $('.input_txt3');
    var $input4 = $('.input_txt4');
    var $input5 = $('.input_txt5');
    var $input_sub = $('.input_sub');
    var $delete = $('.delete');
    var sHandler = '';
    var id = '';
    var sId = 0;

    $a.click(function(){
        sHandler = 'edit';
        id = $(this).parent().siblings().eq(0).html();
        ip = $(this).parent().siblings().eq(1).html();
        hostname = $(this).parent().siblings().eq(2).html();
        describe = $(this).parent().siblings().eq(3).html();
        $pop.find('h3').html('修改节点信息');
        $pop.find('.input_txt3').val(ip);
        $pop.find('.input_txt4').val(hostname);
        $pop.find('.input_txt5').val(describe);
        $pop.show();
    });
    $input_sub.click(function () {
        sHandler = 'insert';
        $pop.find('h3').html('新增节点信息');
        $pop.find('.input_txt3').val("");
        $pop.find('.input_txt4').val("");
        $pop.find('.input_txt5').val("");
        $pop.show();
    });
    $delete.click(function () {
        id = $(this).parent().siblings().eq(0).html();
        $(".mt50").empty();
        $(".mt50").html('<h4 align="center">您确定删除节点信息吗?</h4>');
        sHandler = 'delete';
        $pop.find('form_group mt50').html("");
        $pop.find('h3').html('删除节点信息');
        $pop.show();
    });

    $add.click(function(){
        sHandler = 'add';
        $pop.find('h3').html('新增分类');
        $input.val('');
        $pop.show();
    });

    $cancel.click(function(){
        $pop.hide();
        $error.hide();
        location.reload()
    });

    $input.click(function(){
        $error.hide();
    });

    $confirm.click(function(){
        if(sHandler == "edit"){
            var params = {
            'ip':$(".input_txt3").val(),
            'hostname': $(".input_txt4").val(),
            "id": id,
            "describe":$(".input_txt5").val(),
            "sHandler":sHandler
        };
        // TODO 发起修改分类请求
        $.ajax({
            url: '/nodes_update/',
            type: 'POST',
            dataType: 'json',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(params)
        })
        .done(function(dat) {
            if(dat.status = 'ok'){
                location.reload()
            }else{
                alert("error")
            }
        })
        .fail(function() {
            alert('服务器超时，请重试！');
            });
        }
        else if(sHandler == "insert"){
            var params = {
                'ip':$(".input_txt3").val(),
                'hostname': $(".input_txt4").val(),
                "id": "",
                "describe":$(".input_txt5").val(),
                "sHandler":sHandler
            };
            // TODO 发起修改分类请求
            $.ajax({
                url: '/nodes_update/',
                type: 'POST',
                dataType: 'json',
                contentType:'application/json;charset=UTF-8',
                data:JSON.stringify(params)
            })
            .done(function(dat) {
                if(dat.status = 'ok'){
                    location.reload()
                }else{
                    alert("error")
                }
            })
            .fail(function() {
                alert('服务器超时，请重试！');
            });
        }
        else if(sHandler == "delete"){
            var params = {
                "delete":"1",
                "id": id,
                "sHandler":sHandler
            };
            // TODO 发起修改分类请求
            $.ajax({
                url: '/nodes_update/',
                type: 'POST',
                dataType: 'json',
                contentType:'application/json;charset=UTF-8',
                data:JSON.stringify(params)
            })
            .done(function(dat) {
                if(dat.status = 'ok'){
                    location.reload()
                }else{
                    alert("error")
                }
            })
            .fail(function() {
                alert('服务器超时，请重试！');
            });
        }
    })
});