$(function(){
    $('form.upload-video').on('submit', function(e){
        var $form = $(e.target);
        console.log($form);
        $form.find('input[name=save_changes]')
            .attr('disabled', 'disabled')
            .val(function(){return $(this).data('msg-uploading')});
    })
});
