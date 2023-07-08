class DefinitionError(Exception):
    pass

class ObjCreationFailed(DefinitionError):
    pass

class InsufficientInformation(ObjCreationFailed):
    pass