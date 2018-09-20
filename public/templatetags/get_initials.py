from django import template

register = template.Library()


@register.simple_tag(name='getinitials')
def getinitials(user):
	return "%s%s" % (user.first_name[0], user.last_name[0])
