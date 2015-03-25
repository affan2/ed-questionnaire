(function($){
    $(document).ready(function() {
        var request = {
            type: 'GET',
            url: progress_url + '?nocache=' + new Date().getTime(),
            dataType: 'json',
            success: function(data) {
                var progress = data.progress;
                $('.progress-bar').css('width', progress+'%').attr('aria-valuenow', progress).text(progress+"% complete");
            }
        };

        $.ajax(request);
    });
})(jQuery);
