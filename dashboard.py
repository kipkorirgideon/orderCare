from django.utils.translation import gettext_lazy as _

from grappelli.dashboard import modules, Dashboard, DefaultIndexDashboard


class CustomIndexDashboard(DefaultIndexDashboard):
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.children.append(modules.AppList(
            title=_('The OrderCare Platform'),
            column=1,
            exclude=('django.contrib.*',),
        ))

        self.children.append(modules.AppList(
            title=_('Backend Administration'),
            column=1,
            models=('django.contrib.*',),
        ))
