if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer



@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower()
                    )
    return data



