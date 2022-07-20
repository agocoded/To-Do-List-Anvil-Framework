from ._anvil_designer import AllTasksTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...TaskEdit import TaskEdit

class AllTasksTemplate(AllTasksTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_edit_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(TaskEdit(item = self.item), title="Edit Your Task Details", large=True)
    
    self.refresh_data_bindings()
    pass

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass


