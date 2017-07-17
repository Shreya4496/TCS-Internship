from django import template
register = template.Library()


@register.inclusion_tag('myapp/model_table.html', takes_context=True)
def model_as_table(context, model_key=None, model_table_attrs_key=None):

    if model_key is None:
        model_key = 'object'

    if model_table_attrs_key is None:
        model_table_attrs_key = 'model_table_attrs'

    try:
        attrs = context[model_table_attrs_key]
    except KeyError:
        attrs = context[model_key]._meta.get_all_field_names()

    table_context = {'rows': []}
    for attr in attrs:
        try:
            value = str(getattr(context[model_key], attr))
            if value:
                table_context['rows'].append({'attr': attr,
                                              'value': context[model_key][attr]})
        except AttributeError:
            pass
        # Needs a way to display many_to_many fields.
        except StopIteration:
            pass

    return table_context