from django import forms
from django.contrib import admin

from app.assets.models import *


class TitleAdmin(admin.ModelAdmin):
    """
    Admin for Title model.
    """
    pass

admin.site.register(Title, TitleAdmin)


class MethodAdmin(admin.ModelAdmin):
    """
    Admin for creating methods in the administrator
    page.
    """
    pass

admin.site.register(Method, MethodAdmin)


class QualifierAdminForm(forms.ModelForm):
    class Meta:
        model = Qualifier


class QualifierAdmin(admin.ModelAdmin):
    """
    Admin for defining qualifiers.
    """
    form = QualifierAdminForm

admin.site.register(Qualifier, QualifierAdmin)


class QuantifierAdmin(admin.ModelAdmin):
    """
    Admin for defining quantifiers.
    """
    pass

admin.site.register(Quantifier, QuantifierAdmin)


class ConditionTypeAdmin(admin.ModelAdmin):
    """
    Admin for defining the type of conditions.
    """
    pass

admin.site.register(ConditionType, ConditionTypeAdmin)


class ConditionAdmin(admin.ModelAdmin):
    """
    Admin for creating Conditions.
    """
    pass


class ValueConditionAdmin(admin.ModelAdmin):
    """
    Admin for creating Conditions.
    """
    pass

admin.site.register(ValueCondition, ConditionAdmin)


class ConditionInline(admin.TabularInline):
    model = Condition
    extra = 1


class ConditionGroupAdmin(admin.ModelAdmin):
    """
    Admin for condition groups.
    """
    inlines = [ConditionInline]

admin.site.register(ConditionGroup, ConditionGroupAdmin)


class AttributeConditionAdmin(admin.ModelAdmin):
    """
    Admin for creating Conditions.
    """
    pass

admin.site.register(AttributeCondition, ConditionAdmin)


class ConditionGroupInline(admin.TabularInline):
    model = ConditionGroup
    extra = 1


class AchievementTypeAdmin(admin.ModelAdmin):
    """
    Admin for defining the types of achievements.
    """
    pass

admin.site.register(AchievementType, AchievementTypeAdmin)


class AchievementAdmin(admin.ModelAdmin):
    """
    Admin for creating achievements.
    """
    inlines = [ConditionGroupInline]

admin.site.register(Achievement, AchievementAdmin)
