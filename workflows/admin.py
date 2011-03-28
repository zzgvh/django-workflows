from django.contrib import admin
from workflows.models import State
from workflows.models import StateInheritanceBlock
from workflows.models import StatePermissionRelation
from workflows.models import StateObjectRelation
from workflows.models import Transition
from workflows.models import Workflow
from workflows.models import WorkflowObjectRelation
from workflows.models import WorkflowModelRelation
from workflows.models import WorkflowPermissionRelation

class StateInline(admin.TabularInline):
    model = State


class WorkflowPermissionRelationInline(admin.TabularInline):
    model = WorkflowPermissionRelation
    extra = 0

    
class WorkflowAdmin(admin.ModelAdmin):
    inlines = [
        StateInline, WorkflowPermissionRelationInline,
    ]

admin.site.register(Workflow, WorkflowAdmin)

class StateAdmin(admin.ModelAdmin):
    model = Transition
    list_display = ('name', 'workflow', 'transitions_html',)
    list_filter = ('workflow',)

admin.site.register(State, StateAdmin)
admin.site.register(StateInheritanceBlock)
admin.site.register(StateObjectRelation)


class StatePermissionRelationAdmin(admin.ModelAdmin):
    model = StatePermissionRelation
    list_display = ('state', 'permission', 'role',)
    list_filter = ('state__workflow',)

admin.site.register(StatePermissionRelation, StatePermissionRelationAdmin)


class TransitionAdmin(admin.ModelAdmin):
    model = Transition
    list_display = ('name', 'workflow', 'destination', 'permission', )
    list_filter = ('workflow',)
    
admin.site.register(Transition, TransitionAdmin)


admin.site.register(WorkflowObjectRelation)
admin.site.register(WorkflowModelRelation)
admin.site.register(WorkflowPermissionRelation)

