from django import template

register = template.Library()


@register.filter
def should_display_primary_actions_block(user, submission):
    view_determination_action_displayed = submission.is_determined

    if view_determination_action_displayed:
        return True
    else:
        return False
