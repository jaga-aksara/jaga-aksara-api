from flask import (
    current_app, flash, g, redirect, request, url_for, jsonify
)
import fast_ulid
import mimetypes
import os 
from forms import (TranslatePegonScriptForm)
from http import HTTPStatus
import external_modules as externals 
from externals.jaga_aksara_ai.Integration.JagaAksara import JagaAksara
import json



class PegonScriptController: 
    def translate ():
        file = request.files['photo'] # retrieve the photo attribute from the request
        dirpath = current_app.config['JAGA_AKSARA_PEGON_SCRIPT_IMAGES_DIRECTORY']
        filename = fast_ulid.ulid()
        file_ext = mimetypes.guess_extension(file.mimetype)
        filepath = dirpath + filename + file_ext
        file.save(filepath)

        model = externals.get_jaga_aksara_model()
        translated = model.ocr(filepath)
        
        return jsonify({
            'message': 'Script(s) translated successfully.',
            'data': {
                'translated' : translated, 
            },
            'status': HTTPStatus.OK}), HTTPStatus.OK