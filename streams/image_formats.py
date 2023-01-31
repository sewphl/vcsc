from wagtail.images.formats import Format, register_image_format, unregister_image_format

##Note, update img-responsive to img-fluid 

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image img-fluid full-width', 'width-700'))

unregister_image_format('left')
register_image_format(Format('left', 'Left-aligned', 'richtext-image img-fluid left', 'width-500'))  

unregister_image_format('right')
register_image_format(Format('right', 'Right-aligned', 'richtext-image img-fluid right', 'width-500'))