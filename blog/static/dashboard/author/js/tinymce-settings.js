 tinymce.init({
      selector: '#content',
      max_width: 500,
      max_height: 700,
      min_height: 500,
      min_width: 400,
      plugins: 'autolink lists media table  ' +
          'emoticons anchor pagebreak visualchars code ' +
          'fullscreen autolink lists  charmap print  hr searchreplace ' +
          'wordcount visualblocks table lists fullscreen  ' +
          'insertdatetime  nonbreaking save link image media preview ' +
          'codesample',
      toolbar1: 'checklist table fullscreen preview bold ' +
                'italic underline | fontselect fontsizeselect | forecolor backcolor |' +
                'alignleft alignright | aligncenter alignjustify | indent outdent ' +
                'bullist numlist | link image media | code | emoticons | visualblocks ' +
                'visualchars | charmap hr pagebreak nonbreaking anchor | codesample',
      toolbar_mode: 'floating',
      custom_undo_redo_levels: 20,
       remove_linebreaks: false,
      force_br_newlines: false,
      force_p_newlines: false,
      forced_root_block: '',
      keep_styles: false,
      fix_list_elements:true,
      entity_encoding:"raw",
      extended_valid_elements : '*[*]',
      cleanup: false,
      cleanup_on_startup: false,
      trim_span_elements: false,
      verify_html : false,
      end_container_on_empty_block:true,
      remove_trailing_brs: false,
    });
