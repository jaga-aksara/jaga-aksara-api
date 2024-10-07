import os


from externals.jaga_aksara_ai.Integration.JagaAksara import JagaAksara

_jaga_aksara_model:JagaAksara|None = None

def load_jaga_aksara_model():
    global _jaga_aksara_model
    models_dir = os.getenv('JAGA_AKSARA_MODELS_DIRECTORY')
    _jaga_aksara_model =  JagaAksara(models_dir)

def get_jaga_aksara_model ():
    global _jaga_aksara_model
    if _jaga_aksara_model is None:
        models_dir = os.getenv('JAGA_AKSARA_MODELS_DIRECTORY')
        _jaga_aksara_model =  JagaAksara(models_dir)
    return _jaga_aksara_model
