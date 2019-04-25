def serfed(meta, **kwargs):
    """
    provides flexibility to set fields, exclude and depth at time of instantiating a serializer
    :param meta: self.Meta of a ModelSerializer
    :param kwargs:
    """
    ifields = kwargs.pop('fields', None)
    iexclude = kwargs.pop('exclude', None)
    idepth = kwargs.pop('depth', None)
    if idepth:
        setattr(meta, 'depth', idepth)
    if iexclude:
        setattr(meta, 'exclude', iexclude)
    elif ifields:
        setattr(meta, 'fields', ifields)
    else:
        setattr(meta, 'fields', '__all__')
