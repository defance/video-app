$(function(){
    $('form.upload-video').on('submit', function(e){
        var $form = $(e.target);
        $form.find('input[name=save_changes]')
            .attr('disabled', 'disabled')
            .val(function(){return $(this).data('msg-uploading')});
    });
    $('form.upload-video input[type=submit]').on('click', function(e) {
        var $form = $(e.target).closest('form');
        var $id_input = $form.find('input[name=id]');
        if($id_input.val() == ''){
            $id_input.val($id_input.attr('placeholder'));
        }
    });
});
