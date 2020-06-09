from wtforms import Form, SelectField, SubmitField


class PeopleFilterForm(Form):
    filter = SubmitField('Filter')
    vehicle = SelectField(label='Vehicle:')
    planet = SelectField(label='Planet:')
    film = SelectField(label='Film:', )
    starship = SelectField(label='Starship:')