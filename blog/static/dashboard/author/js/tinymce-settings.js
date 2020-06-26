 tinymce.init({
      selector: '#body',
      max_width: 500,
      max_height: 700,
      min_height: 500,
      min_width: 400,
      plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists ' +
          'checklist media mediaembed pageembed permanentpen powerpaste table advtable ' +
          'tinymcespellchecker emoticons anchor pagebreak visualchars code ' +
          'fullscreen autolink lists  charmap print  hr contextmenu directionality ' +
          'searchreplace wordcount visualblocks table lists fullscreen  ' +
          'insertdatetime  nonbreaking textcolor save link image media preview ' +
          'codesample contextmenu',
      toolbar1: 'a11ycheck casechange checklist code ' +
                'formatpainter pageembed permanentpen table fullscreen preview bold ' +
                'italic underline fontselect fontsizeselect forecolor backcolor ' +
                'alignleft alignright aligncenter alignjustify indent outdent ' +
                'bullist numlist table link image media codesample emoticons visualblocks ' +
                'visualchars charmap hr pagebreak nonbreaking anchor code ',
      toolbar_mode: 'floating',
      contextmenu: 'formats link image',
      custom_undo_redo_levels: 20,
    });
